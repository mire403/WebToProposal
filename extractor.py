"""关键信息抽取模块"""

import json
import logging
from typing import Dict, List, Any
from openai import OpenAI

from .prompts import EXTRACTION_PROMPT
from .utils import chunk_text

logger = logging.getLogger(__name__)


class InformationExtractor:
    """信息抽取器，从网页内容中提取关键信息"""
    
    def __init__(self, api_key: str = None, base_url: str = None, model: str = "gpt-3.5-turbo"):
        """
        初始化抽取器
        
        Args:
            api_key: OpenAI API Key（如果使用 OpenAI）
            base_url: API 基础 URL（如果使用兼容 API）
            model: 模型名称
        """
        self.model = model
        self.client = None
        
        # 尝试初始化 OpenAI 客户端
        try:
            if api_key:
                self.client = OpenAI(api_key=api_key, base_url=base_url)
            else:
                # 尝试从环境变量读取
                import os
                api_key = os.getenv('OPENAI_API_KEY')
                if api_key:
                    self.client = OpenAI(api_key=api_key, base_url=base_url)
        except Exception as e:
            logger.warning(f"Failed to initialize OpenAI client: {e}")
            logger.warning("Will use mock extraction mode")
    
    def extract(self, page_data: Dict[str, str]) -> Dict[str, Any]:
        """
        从单个网页中提取关键信息
        
        Args:
            page_data: 包含 url, title, content 的字典
            
        Returns:
            提取的结构化信息
        """
        if not self.client:
            # 如果没有 LLM，使用简单的关键词提取
            return self._simple_extract(page_data)
        
        try:
            prompt = EXTRACTION_PROMPT.format(
                title=page_data.get('title', ''),
                url=page_data.get('url', ''),
                content=page_data.get('content', '')[:8000]  # 限制长度
            )
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是一个专业的信息提取助手，只提取网页中的实际内容，不编造信息。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                response_format={"type": "json_object"}
            )
            
            result_text = response.choices[0].message.content
            result = json.loads(result_text)
            
            return {
                'url': page_data.get('url'),
                'title': page_data.get('title'),
                'extracted': result
            }
            
        except Exception as e:
            logger.error(f"Extraction failed for {page_data.get('url')}: {e}")
            return self._simple_extract(page_data)
    
    def _simple_extract(self, page_data: Dict[str, str]) -> Dict[str, Any]:
        """简单的关键词提取（当没有 LLM 时使用）"""
        content = page_data.get('content', '')
        title = page_data.get('title', '')
        
        # 简单的段落提取
        paragraphs = [p.strip() for p in content.split('\n\n') if len(p.strip()) > 50]
        
        return {
            'url': page_data.get('url'),
            'title': title,
            'extracted': {
                'key_facts': paragraphs[:5],
                'key_arguments': paragraphs[5:10] if len(paragraphs) > 5 else [],
                'problems': []
            }
        }
    
    def extract_multiple(self, pages_data: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        """
        批量提取多个网页的信息
        
        Args:
            pages_data: 网页数据列表
            
        Returns:
            提取结果列表
        """
        results = []
        for page_data in pages_data:
            result = self.extract(page_data)
            if result:
                results.append(result)
        return results
