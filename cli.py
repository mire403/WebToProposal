"""命令行入口"""

import argparse
import sys
import os
from pathlib import Path

from webtoproposal.crawler import WebCrawler
from webtoproposal.extractor import InformationExtractor
from webtoproposal.merger import InformationMerger
from webtoproposal.planner import ProposalPlanner
from webtoproposal.writer import ProposalWriter
from webtoproposal.utils import setup_logging

def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='WebToProposal - Turn multiple web pages into a structured proposal'
    )
    parser.add_argument(
        'input',
        type=str,
        help='输入文件路径（每行一个 URL）'
    )
    parser.add_argument(
        '--out',
        type=str,
        default='proposal.md',
        help='输出文件路径（默认：proposal.md）'
    )
    parser.add_argument(
        '--api-key',
        type=str,
        default=None,
        help='OpenAI API Key（也可通过环境变量 OPENAI_API_KEY 设置）'
    )
    parser.add_argument(
        '--base-url',
        type=str,
        default=None,
        help='API 基础 URL（用于兼容 OpenAI API 的服务）'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='gpt-3.5-turbo',
        help='使用的模型名称（默认：gpt-3.5-turbo）'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='显示详细日志'
    )
    
    args = parser.parse_args()
    
    # 设置日志
    log_level = 'DEBUG' if args.verbose else 'INFO'
    setup_logging(log_level)
    
    # 读取 URL 列表
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"错误：输入文件不存在：{args.input}")
        sys.exit(1)
    
    with open(input_path, 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip()]
    
    if not urls:
        print("错误：输入文件中没有有效的 URL")
        sys.exit(1)
    
    print(f"读取到 {len(urls)} 个 URL")
    print("=" * 50)
    
    # 初始化组件
    print("1. 开始抓取网页...")
    crawler = WebCrawler()
    pages_data = crawler.fetch_multiple(urls)
    
    if not pages_data:
        print("错误：未能抓取到任何网页内容")
        sys.exit(1)
    
    print(f"成功抓取 {len(pages_data)} 个网页")
    print("=" * 50)
    
    # 初始化 LLM 组件
    api_key = args.api_key or os.getenv('OPENAI_API_KEY')
    extractor = InformationExtractor(api_key=api_key, base_url=args.base_url, model=args.model)
    merger = InformationMerger(extractor=extractor)
    planner = ProposalPlanner(extractor=extractor)
    writer = ProposalWriter(extractor=extractor)
    
    # 提取信息
    print("2. 开始提取关键信息...")
    extracted_data = extractor.extract_multiple(pages_data)
    print(f"完成 {len(extracted_data)} 个网页的信息提取")
    print("=" * 50)
    
    # 融合信息
    print("3. 开始融合多网页信息...")
    merged_info = merger.merge(extracted_data)
    print("信息融合完成")
    print("=" * 50)
    
    # 规划方案
    print("4. 开始规划方案结构...")
    plan = planner.plan(merged_info)
    print("方案结构规划完成")
    print("=" * 50)
    
    # 生成方案
    print("5. 开始生成方案文档...")
    proposal_title = f"基于 {len(pages_data)} 个网页的方案初稿"
    proposal_text = writer.write(plan, title=proposal_title)
    print("方案文档生成完成")
    print("=" * 50)
    
    # 保存输出
    output_path = Path(args.out)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(proposal_text)
    
    print(f"\n✅ 完成！方案已保存至：{output_path}")
    print(f"   共处理 {len(pages_data)} 个网页")
    
    if not api_key:
        print("\n⚠️  提示：未设置 API Key，使用了简化模式。")
        print("   设置 OPENAI_API_KEY 环境变量或使用 --api-key 参数可获得更好的效果。")

if __name__ == '__main__':
    main()
