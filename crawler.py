"""网页抓取与清洗模块"""

import requests
from bs4 import BeautifulSoup
from typing import Dict, Optional
import logging
from urllib.parse import urljoin, urlparse

from .utils import clean_text, validate_url

logger = logging.getLogger(__name__)


class WebCrawler:
    """网页爬虫，负责抓取和清洗网页内容"""
    
    def __init__(self, timeout: int = 10, headers: Optional[Dict] = None):
        """
        初始化爬虫
        
        Args:
            timeout: 请求超时时间（秒）
            headers: 自定义请求头
        """
        self.timeout = timeout
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def fetch(self, url: str) -> Optional[Dict[str, str]]:
        """
        抓取单个网页
        
        Args:
            url: 网页 URL
            
        Returns:
            包含 title 和 content 的字典，失败返回 None
        """
        if not validate_url(url):
            logger.warning(f"Invalid URL: {url}")
            return None
        
        try:
            logger.info(f"Fetching: {url}")
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            response.encoding = response.apparent_encoding or 'utf-8'
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 提取标题
            title = self._extract_title(soup)
            
            # 提取正文
            content = self._extract_content(soup)
            
            if not content:
                logger.warning(f"No content extracted from: {url}")
                return None
            
            return {
                'url': url,
                'title': title,
                'content': content
            }
            
        except requests.RequestException as e:
            logger.error(f"Failed to fetch {url}: {e}")
            return None
        except Exception as e:
            logger.error(f"Error processing {url}: {e}")
            return None
    
    def _extract_title(self, soup: BeautifulSoup) -> str:
        """提取页面标题"""
        # 尝试多种标题选择器
        title_selectors = [
            'h1',
            'title',
            'meta[property="og:title"]',
            'meta[name="title"]'
        ]
        
        for selector in title_selectors:
            element = soup.select_one(selector)
            if element:
                title = element.get_text() if hasattr(element, 'get_text') else element.get('content', '')
                if title:
                    return clean_text(title)
        
        return "无标题"
    
    def _extract_content(self, soup: BeautifulSoup) -> str:
        """提取页面正文内容"""
        # 移除不需要的标签
        for tag in soup(['script', 'style', 'nav', 'header', 'footer', 
                        'aside', 'advertisement', 'ad', 'noscript']):
            tag.decompose()
        
        # 尝试找到主要内容区域
        main_content = None
        
        # 常见的内容容器选择器
        content_selectors = [
            'article',
            'main',
            '[role="main"]',
            '.content',
            '.post-content',
            '.article-content',
            '#content',
            '#main-content'
        ]
        
        for selector in content_selectors:
            element = soup.select_one(selector)
            if element:
                main_content = element
                break
        
        # 如果没有找到特定容器，使用 body
        if not main_content:
            main_content = soup.find('body')
        
        if not main_content:
            return ""
        
        # 提取所有段落文本
        paragraphs = []
        for p in main_content.find_all(['p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            text = p.get_text(strip=True)
            if text and len(text) > 10:  # 过滤太短的文本
                paragraphs.append(text)
        
        # 合并段落
        content = '\n\n'.join(paragraphs)
        return clean_text(content)
    
    def fetch_multiple(self, urls: list) -> list:
        """
        批量抓取多个网页
        
        Args:
            urls: URL 列表
            
        Returns:
            成功抓取的网页内容列表
        """
        results = []
        for url in urls:
            result = self.fetch(url)
            if result:
                results.append(result)
        return results
