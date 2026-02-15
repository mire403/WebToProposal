"""方案结构规划模块"""

import json
import logging
from typing import Dict, Any

from .prompts import PLANNING_PROMPT
from .extractor import InformationExtractor

logger = logging.getLogger(__name__)


class ProposalPlanner:
    """方案规划器，根据融合后的信息规划方案结构"""
    
    def __init__(self, extractor: InformationExtractor = None):
        """
        初始化规划器
        
        Args:
            extractor: 信息抽取器实例（用于调用 LLM）
        """
        self.extractor = extractor
    
    def plan(self, merged_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        规划方案结构
        
        Args:
            merged_info: 融合后的信息
            
        Returns:
            规划好的方案结构
        """
        if not merged_info:
            return self._default_plan()
        
        if not self.extractor or not self.extractor.client:
            # 如果没有 LLM，使用简单规划
            return self._simple_plan(merged_info)
        
        try:
            # 格式化融合信息
            info_text = self._format_merged_info(merged_info)
            
            prompt = PLANNING_PROMPT.format(merged_info=info_text)
            
            response = self.extractor.client.chat.completions.create(
                model=self.extractor.model,
                messages=[
                    {"role": "system", "content": "你是一个专业的方案规划助手，所有内容必须基于提供的信息，不要编造。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                response_format={"type": "json_object"}
            )
            
            result_text = response.choices[0].message.content
            result = json.loads(result_text)
            
            return result
            
        except Exception as e:
            logger.error(f"Planning failed: {e}")
            return self._simple_plan(merged_info)
    
    def _format_merged_info(self, merged_info: Dict[str, Any]) -> str:
        """格式化融合信息为文本"""
        formatted = []
        
        common_info = merged_info.get('common_info', {})
        unique_info = merged_info.get('unique_info', {})
        themes = merged_info.get('themes', [])
        
        formatted.append("共同信息：")
        formatted.append(f"  事实: {', '.join(common_info.get('facts', []))}")
        formatted.append(f"  观点: {', '.join(common_info.get('arguments', []))}")
        formatted.append(f"  问题: {', '.join(common_info.get('problems', []))}")
        formatted.append("")
        
        formatted.append("独特信息：")
        formatted.append(f"  事实: {', '.join(unique_info.get('facts', []))}")
        formatted.append(f"  观点: {', '.join(unique_info.get('arguments', []))}")
        formatted.append(f"  问题: {', '.join(unique_info.get('problems', []))}")
        formatted.append("")
        
        formatted.append(f"主题: {', '.join(themes)}")
        
        return "\n".join(formatted)
    
    def _simple_plan(self, merged_info: Dict[str, Any]) -> Dict[str, Any]:
        """简单的方案规划（当没有 LLM 时使用）"""
        common_info = merged_info.get('common_info', {})
        unique_info = merged_info.get('unique_info', {})
        
        all_facts = common_info.get('facts', []) + unique_info.get('facts', [])
        all_arguments = common_info.get('arguments', []) + unique_info.get('arguments', [])
        all_problems = common_info.get('problems', []) + unique_info.get('problems', [])
        
        return {
            'background': {
                'main_points': all_facts[:5],
                'key_facts': all_facts[:3]
            },
            'current_situation': {
                'main_points': all_arguments[:5],
                'analysis': all_arguments[:3]
            },
            'key_problems': {
                'problems': all_problems[:5],
                'impact': all_problems[:3] if len(all_problems) >= 3 else all_problems
            },
            'proposed_solutions': {
                'solutions': all_arguments[-3:] if len(all_arguments) >= 3 else all_arguments,
                'rationale': []
            }
        }
    
    def _default_plan(self) -> Dict[str, Any]:
        """默认方案结构"""
        return {
            'background': {
                'main_points': [],
                'key_facts': []
            },
            'current_situation': {
                'main_points': [],
                'analysis': []
            },
            'key_problems': {
                'problems': [],
                'impact': []
            },
            'proposed_solutions': {
                'solutions': [],
                'rationale': []
            }
        }
