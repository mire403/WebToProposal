"""工具函数模块"""

import logging
from typing import List, Dict, Any
import re


def setup_logging(level=logging.INFO):
    """设置日志"""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def clean_text(text: str) -> str:
    """清理文本：去除多余空白、换行等"""
    if not text:
        return ""
    # 去除多余空白
    text = re.sub(r'\s+', ' ', text)
    # 去除首尾空白
    text = text.strip()
    return text


def chunk_text(text: str, max_length: int = 4000) -> List[str]:
    """将长文本分块，避免超过 LLM 上下文限制"""
    if len(text) <= max_length:
        return [text]
    
    chunks = []
    sentences = re.split(r'[。！？\n]', text)
    current_chunk = ""
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        
        if len(current_chunk) + len(sentence) + 1 <= max_length:
            current_chunk += sentence + "。"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence + "。"
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks


def validate_url(url: str) -> bool:
    """验证 URL 格式"""
    pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return pattern.match(url) is not None
