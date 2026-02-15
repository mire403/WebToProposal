"""方案文本生成模块"""

import logging
from typing import Dict, Any

from .prompts import WRITING_PROMPT
from .extractor import InformationExtractor

logger = logging.getLogger(__name__)


class ProposalWriter:
    """方案撰写器，根据规划结构生成最终方案文本"""
    
    def __init__(self, extractor: InformationExtractor = None):
        """
        初始化撰写器
        
        Args:
            extractor: 信息抽取器实例（用于调用 LLM）
        """
        self.extractor = extractor
    
    def write(self, plan: Dict[str, Any], title: str = "方案初稿") -> str:
        """
        根据规划结构撰写方案
        
        Args:
            plan: 规划好的方案结构
            title: 方案标题
            
        Returns:
            完整的方案文本（Markdown 格式）
        """
        if not self.extractor or not self.extractor.client:
            # 如果没有 LLM，使用模板生成
            return self._template_write(plan, title)
        
        try:
            # 格式化规划结构
            plan_text = self._format_plan(plan)
            
            prompt = WRITING_PROMPT.format(plan=plan_text)
            
            response = self.extractor.client.chat.completions.create(
                model=self.extractor.model,
                messages=[
                    {"role": "system", "content": "你是一个专业的方案撰写助手，风格正式、客观、条理清晰，适合办公场景使用。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5
            )
            
            result_text = response.choices[0].message.content
            
            # 确保标题正确
            if not result_text.startswith('#'):
                result_text = f"# {title}\n\n{result_text}"
            else:
                # 替换第一个标题
                lines = result_text.split('\n')
                lines[0] = f"# {title}"
                result_text = '\n'.join(lines)
            
            return result_text
            
        except Exception as e:
            logger.error(f"Writing failed: {e}")
            return self._template_write(plan, title)
    
    def _format_plan(self, plan: Dict[str, Any]) -> str:
        """格式化规划结构为文本"""
        formatted = []
        
        background = plan.get('background', {})
        formatted.append("背景：")
        formatted.append(f"  要点: {', '.join(background.get('main_points', []))}")
        formatted.append(f"  关键事实: {', '.join(background.get('key_facts', []))}")
        formatted.append("")
        
        current_situation = plan.get('current_situation', {})
        formatted.append("现状分析：")
        formatted.append(f"  要点: {', '.join(current_situation.get('main_points', []))}")
        formatted.append(f"  分析: {', '.join(current_situation.get('analysis', []))}")
        formatted.append("")
        
        key_problems = plan.get('key_problems', {})
        formatted.append("核心问题：")
        formatted.append(f"  问题: {', '.join(key_problems.get('problems', []))}")
        formatted.append(f"  影响: {', '.join(key_problems.get('impact', []))}")
        formatted.append("")
        
        proposed_solutions = plan.get('proposed_solutions', {})
        formatted.append("可行方案：")
        formatted.append(f"  方案: {', '.join(proposed_solutions.get('solutions', []))}")
        formatted.append(f"  理由: {', '.join(proposed_solutions.get('rationale', []))}")
        
        return "\n".join(formatted)
    
    def _template_write(self, plan: Dict[str, Any], title: str) -> str:
        """使用模板生成方案（当没有 LLM 时使用）"""
        lines = [f"# {title}", ""]
        
        # 背景
        lines.append("## 一、背景")
        lines.append("")
        background = plan.get('background', {})
        if background.get('key_facts'):
            lines.append("基于收集的信息，相关背景如下：")
            lines.append("")
            for fact in background.get('key_facts', [])[:5]:
                lines.append(f"- {fact}")
        else:
            lines.append("（待补充背景信息）")
        lines.append("")
        
        # 现状分析
        lines.append("## 二、现状分析")
        lines.append("")
        current_situation = plan.get('current_situation', {})
        if current_situation.get('main_points'):
            lines.append("当前情况分析如下：")
            lines.append("")
            for point in current_situation.get('main_points', [])[:5]:
                lines.append(f"- {point}")
        else:
            lines.append("（待补充现状信息）")
        lines.append("")
        
        # 核心问题
        lines.append("## 三、核心问题总结")
        lines.append("")
        key_problems = plan.get('key_problems', {})
        if key_problems.get('problems'):
            lines.append("通过分析，主要问题包括：")
            lines.append("")
            for problem in key_problems.get('problems', [])[:5]:
                lines.append(f"- {problem}")
        else:
            lines.append("（待补充问题信息）")
        lines.append("")
        
        # 可行方案
        lines.append("## 四、可行方案建议")
        lines.append("")
        proposed_solutions = plan.get('proposed_solutions', {})
        if proposed_solutions.get('solutions'):
            lines.append("基于以上分析，建议采取以下方案：")
            lines.append("")
            for solution in proposed_solutions.get('solutions', [])[:5]:
                lines.append(f"- {solution}")
        else:
            lines.append("（待补充方案信息）")
        lines.append("")
        
        return "\n".join(lines)
