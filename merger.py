"""多网页信息融合模块"""

import json
import logging
from typing import Dict, List, Any

from .prompts import MERGE_PROMPT
from .extractor import InformationExtractor

logger = logging.getLogger(__name__)


class InformationMerger:
    """信息融合器，合并多个网页的信息"""
    
    def __init__(self, extractor: InformationExtractor = None):
        """
        初始化融合器
        
        Args:
            extractor: 信息抽取器实例（用于调用 LLM）
        """
        self.extractor = extractor
    
    def merge(self, extracted_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        融合多个网页的提取信息
        
        Args:
            extracted_data: 提取的信息列表
            
        Returns:
            融合后的信息
        """
        if not extracted_data:
            return {}
        
        if len(extracted_data) == 1:
            # 只有一个网页，直接返回
            return {
                'common_info': extracted_data[0].get('extracted', {}),
                'unique_info': {},
                'themes': []
            }
        
        if not self.extractor or not self.extractor.client:
            # 如果没有 LLM，使用简单合并
            return self._simple_merge(extracted_data)
        
        try:
            # 格式化提取的信息
            info_text = self._format_extracted_info(extracted_data)
            
            prompt = MERGE_PROMPT.format(
                count=len(extracted_data),
                extracted_info=info_text
            )
            
            response = self.extractor.client.chat.completions.create(
                model=self.extractor.model,
                messages=[
                    {"role": "system", "content": "你是一个专业的信息整合助手，只基于提供的信息进行整理，不添加新内容。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                response_format={"type": "json_object"}
            )
            
            result_text = response.choices[0].message.content
            result = json.loads(result_text)
            
            return result
            
        except Exception as e:
            logger.error(f"Merge failed: {e}")
            return self._simple_merge(extracted_data)
    
    def _format_extracted_info(self, extracted_data: List[Dict[str, Any]]) -> str:
        """格式化提取的信息为文本"""
        formatted = []
        for i, data in enumerate(extracted_data, 1):
            extracted = data.get('extracted', {})
            formatted.append(f"网页 {i} ({data.get('title', '无标题')}):")
            formatted.append(f"  关键事实: {', '.join(extracted.get('key_facts', []))}")
            formatted.append(f"  重要论述: {', '.join(extracted.get('key_arguments', []))}")
            formatted.append(f"  问题: {', '.join(extracted.get('problems', []))}")
            formatted.append("")
        
        return "\n".join(formatted)
    
    def _simple_merge(self, extracted_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """简单的信息合并（当没有 LLM 时使用）"""
        all_facts = []
        all_arguments = []
        all_problems = []
        
        for data in extracted_data:
            extracted = data.get('extracted', {})
            all_facts.extend(extracted.get('key_facts', []))
            all_arguments.extend(extracted.get('key_arguments', []))
            all_problems.extend(extracted.get('problems', []))
        
        # 简单去重
        all_facts = list(set(all_facts))
        all_arguments = list(set(all_arguments))
        all_problems = list(set(all_problems))
        
        return {
            'common_info': {
                'facts': all_facts[:10],
                'arguments': all_arguments[:10],
                'problems': all_problems[:5]
            },
            'unique_info': {
                'facts': [],
                'arguments': [],
                'problems': []
            },
            'themes': []
        }
