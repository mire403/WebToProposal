<div align="center">

#  WebToProposal


**🌐 网页信息自动写方案** | Turn multiple web pages into a structured proposal

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenAI](https://img.shields.io/badge/OpenAI-Compatible-orange.svg)](https://openai.com/)

*让 AI 帮你把网页资料整理成专业方案，告别复制粘贴的苦日子！* ✨

</div>

---

## 📖 项目简介

### 🎯 解决的真实痛点

你是否经历过这样的场景？

> 💼 **写项目申报书**：需要收集大量政策文件、行业报告、新闻资讯，然后手动整理成背景、现状、问题、方案...  
> 📊 **写商业方案**：从多个网站找资料，复制粘贴到 Word，再人工梳理逻辑结构...  
> 📝 **写调研报告**：浏览几十个网页，把关键信息摘出来，再组织成文档...

**传统流程**：
1. 🔍 到处搜索网页资料
2. 📋 复制粘贴到文档
3. ✂️ 人工整理背景 / 现状 / 问题
4. ✍️ 再自己"编"方案结构

**结果**：耗时数小时甚至数天，而且高度重复！😫

### ✨ WebToProposal 的解决方案

**输入**：多个 URL（新闻、官网、报告、政策页面等）  
**输出**：一份结构化「方案初稿」，包含：
- 📌 **背景**：基于网页信息整理的背景描述
- 📊 **现状分析**：当前情况的客观分析
- ⚠️ **核心问题总结**：识别出的关键问题
- 💡 **可行方案建议**：基于信息的方案思路

**核心价值**：
- ⏱️ **节省时间**：从数小时缩短到几分钟
- 🎯 **结构化输出**：固定格式，直接可用
- 🧠 **智能融合**：自动去重、归纳、整理
- 📄 **办公风格**：正式、客观、条理清晰

---

## 🎨 典型使用场景

### 1️⃣ 项目申报书撰写 📝

**场景**：需要申报政府项目，要求写项目背景、现状分析、问题识别、解决方案

**使用方式**：
```bash
# 准备包含政策文件、行业报告的 URL 列表
python cli.py project_urls.txt --out project_proposal.md
```

**效果**：自动整理出符合申报要求的方案初稿，只需微调即可提交

### 2️⃣ 商业方案撰写 💼

**场景**：向客户提交商业方案，需要整合市场调研、竞品分析、政策支持等信息

**使用方式**：
```bash
# 输入市场报告、竞品网站、政策页面等 URL
python cli.py business_urls.txt --out business_proposal.md
```

**效果**：快速生成结构化的商业方案框架，节省大量整理时间

### 3️⃣ 产品方案撰写 📦

**场景**：新产品立项，需要整理技术趋势、市场需求、可行性分析

**使用方式**：
```bash
# 输入技术博客、市场分析、用户调研等 URL
python cli.py product_urls.txt --out product_proposal.md
```

**效果**：自动归纳技术背景、市场现状、核心问题、产品方案

### 4️⃣ 调研报告撰写 📊

**场景**：行业调研、可行性分析，需要整合多个来源的信息

**使用方式**：
```bash
# 输入行业报告、新闻资讯、政策文件等 URL
python cli.py research_urls.txt --out research_report.md
```

**效果**：快速生成结构化的调研报告初稿

---

## 🏗️ 技术架构

### 📐 系统架构图

```
┌─────────────────────────────────────────────────────────┐
│                    CLI 命令行入口                         │
│                    (cli.py)                              │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              1. 网页抓取模块 (crawler.py)                │
│  ┌──────────────────────────────────────────────────┐  │
│  │ • requests 发送 HTTP 请求                        │  │
│  │ • BeautifulSoup 解析 HTML                        │  │
│  │ • 智能提取正文（过滤广告、导航）                  │  │
│  │ • 提取标题和关键段落                             │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           2. 信息抽取模块 (extractor.py)                 │
│  ┌──────────────────────────────────────────────────┐  │
│  │ • LLM 智能提取关键信息（可选）                    │  │
│  │ • 提取：关键事实、重要论述、问题描述              │  │
│  │ • 简化模式：基于规则的提取（无 LLM）              │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           3. 信息融合模块 (merger.py)                    │
│  ┌──────────────────────────────────────────────────┐  │
│  │ • 识别共性信息（多个网页都提到的内容）             │  │
│  │ • 去除重复内容                                    │  │
│  │ • 保留独特视角（不同来源的独特观点）               │  │
│  │ • 按主题分类归纳                                  │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           4. 方案规划模块 (planner.py)                   │
│  ┌──────────────────────────────────────────────────┐  │
│  │ • 根据融合信息规划方案结构                        │  │
│  │ • 固定输出格式：                                 │  │
│  │   - 背景 (Background)                            │  │
│  │   - 现状分析 (Current Situation)                │  │
│  │   - 核心问题 (Key Problems)                     │  │
│  │   - 可行方案 (Proposed Solutions)               │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           5. 方案生成模块 (writer.py)                    │
│  ┌──────────────────────────────────────────────────┐  │
│  │ • 根据规划结构生成最终方案文本                    │  │
│  │ • 使用正式、客观的办公文档风格                    │  │
│  │ • 输出 Markdown 格式                             │  │
│  │ • 段落 + 条列结合                                │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
              📄 方案初稿 (proposal.md)
```

### 🔧 核心模块详解

#### 1. 网页抓取模块 (`crawler.py`)

**功能**：智能抓取网页内容，自动过滤噪音

**核心代码解析**：

```python
class WebCrawler:
    """网页爬虫，负责抓取和清洗网页内容"""
    
    def fetch(self, url: str) -> Optional[Dict[str, str]]:
        """
        抓取单个网页的核心逻辑
        """
        # 1. 验证 URL 格式
        if not validate_url(url):
            return None
        
        # 2. 发送 HTTP 请求（带超时和自定义 User-Agent）
        response = requests.get(url, headers=self.headers, timeout=self.timeout)
        response.encoding = response.apparent_encoding or 'utf-8'
        
        # 3. 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 4. 移除不需要的标签（广告、导航、脚本等）
        for tag in soup(['script', 'style', 'nav', 'header', 'footer', 
                        'aside', 'advertisement', 'ad', 'noscript']):
            tag.decompose()
        
        # 5. 智能查找主要内容区域
        # 优先查找：article > main > [role="main"] > .content > body
        main_content = self._find_main_content(soup)
        
        # 6. 提取所有段落文本
        paragraphs = []
        for p in main_content.find_all(['p', 'div', 'h1', 'h2', 'h3']):
            text = p.get_text(strip=True)
            if text and len(text) > 10:  # 过滤太短的文本
                paragraphs.append(text)
        
        return {
            'url': url,
            'title': self._extract_title(soup),
            'content': '\n\n'.join(paragraphs)
        }
```

**技术亮点**：
- ✅ 自动识别编码，避免乱码
- ✅ 智能过滤广告和导航元素
- ✅ 优先提取主要内容区域（article、main 等语义标签）
- ✅ 保留标题层级结构（h1-h6）

#### 2. 信息抽取模块 (`extractor.py`)

**功能**：从网页内容中提取结构化信息

**核心代码解析**：

```python
class InformationExtractor:
    """信息抽取器，从网页内容中提取关键信息"""
    
    def extract(self, page_data: Dict[str, str]) -> Dict[str, Any]:
        """
        使用 LLM 智能提取关键信息
        """
        # 1. 构建提取 Prompt（来自 prompts.py）
        prompt = EXTRACTION_PROMPT.format(
            title=page_data.get('title', ''),
            url=page_data.get('url', ''),
            content=page_data.get('content', '')[:8000]  # 限制长度避免超出 token 限制
        )
        
        # 2. 调用 LLM API（支持 OpenAI 和兼容 API）
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "你是一个专业的信息提取助手..."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,  # 低温度保证输出稳定
            response_format={"type": "json_object"}  # 强制 JSON 格式输出
        )
        
        # 3. 解析 JSON 结果
        result = json.loads(response.choices[0].message.content)
        
        # 返回结构化信息：
        # {
        #     "key_facts": ["事实1", "事实2", ...],
        #     "key_arguments": ["论述1", "论述2", ...],
        #     "problems": ["问题1", "问题2", ...]
        # }
        return result
```

**技术亮点**：
- ✅ 支持 LLM 智能提取（GPT-3.5/4 等）
- ✅ 无 LLM 时自动降级到简化模式
- ✅ 强制 JSON 格式输出，便于后续处理
- ✅ 低温度设置，保证提取准确性

**简化模式**（无 LLM 时）：
```python
def _simple_extract(self, page_data: Dict[str, str]) -> Dict[str, Any]:
    """简单的关键词提取（当没有 LLM 时使用）"""
    content = page_data.get('content', '')
    paragraphs = [p.strip() for p in content.split('\n\n') if len(p.strip()) > 50]
    
    return {
        'key_facts': paragraphs[:5],
        'key_arguments': paragraphs[5:10],
        'problems': []
    }
```

#### 3. 信息融合模块 (`merger.py`)

**功能**：合并多个网页的信息，去重、聚类、归纳

**核心代码解析**：

```python
class InformationMerger:
    """信息融合器，合并多个网页的信息"""
    
    def merge(self, extracted_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        融合多个网页的提取信息
        """
        # 1. 格式化所有提取的信息
        info_text = self._format_extracted_info(extracted_data)
        # 输出格式：
        # 网页 1 (标题1):
        #   关键事实: 事实1, 事实2, ...
        #   重要论述: 论述1, 论述2, ...
        #   问题: 问题1, 问题2, ...
        
        # 2. 使用 LLM 进行智能融合
        prompt = MERGE_PROMPT.format(
            count=len(extracted_data),
            extracted_info=info_text
        )
        
        response = self.extractor.client.chat.completions.create(
            model=self.extractor.model,
            messages=[...],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        # 3. 返回融合结果：
        # {
        #     "common_info": {
        #         "facts": ["共同事实1", ...],
        #         "arguments": ["共同观点1", ...],
        #         "problems": ["共同问题1", ...]
        #     },
        #     "unique_info": {
        #         "facts": ["独特事实1", ...],
        #         ...
        #     },
        #     "themes": ["主题1", "主题2", ...]
        # }
        return json.loads(response.choices[0].message.content)
```

**技术亮点**：
- ✅ 自动识别共性信息（多个网页都提到的内容）
- ✅ 智能去重，避免重复内容
- ✅ 保留独特视角（不同来源的独特观点）
- ✅ 主题聚类，便于后续规划

#### 4. 方案规划模块 (`planner.py`)

**功能**：根据融合后的信息规划方案结构

**核心代码解析**：

```python
class ProposalPlanner:
    """方案规划器，根据融合后的信息规划方案结构"""
    
    def plan(self, merged_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        规划方案结构（固定四部分）
        """
        # 1. 格式化融合信息
        info_text = self._format_merged_info(merged_info)
        
        # 2. 使用 LLM 规划结构
        prompt = PLANNING_PROMPT.format(merged_info=info_text)
        
        response = self.extractor.client.chat.completions.create(...)
        
        # 3. 返回规划结构：
        # {
        #     "background": {
        #         "main_points": ["要点1", ...],
        #         "key_facts": ["关键事实1", ...]
        #     },
        #     "current_situation": {
        #         "main_points": ["要点1", ...],
        #         "analysis": ["分析1", ...]
        #     },
        #     "key_problems": {
        #         "problems": ["问题1", ...],
        #         "impact": ["影响1", ...]
        #     },
        #     "proposed_solutions": {
        #         "solutions": ["方案1", ...],
        #         "rationale": ["理由1", ...]
        #     }
        # }
        return result
```

**固定输出结构**：
- 📌 **背景 (Background)**：基于信息中的事实和背景描述
- 📊 **现状分析 (Current Situation)**：基于信息中的现状描述和分析
- ⚠️ **核心问题总结 (Key Problems)**：基于信息中提到的问题
- 💡 **可行方案建议 (Proposed Solutions)**：基于信息中的建议和方案思路

#### 5. 方案生成模块 (`writer.py`)

**功能**：根据规划结构生成最终方案文本

**核心代码解析**：

```python
class ProposalWriter:
    """方案撰写器，根据规划结构生成最终方案文本"""
    
    def write(self, plan: Dict[str, Any], title: str = "方案初稿") -> str:
        """
        根据规划结构撰写方案
        """
        # 1. 格式化规划结构
        plan_text = self._format_plan(plan)
        
        # 2. 使用 LLM 生成正式文档
        prompt = WRITING_PROMPT.format(plan=plan_text)
        
        response = self.extractor.client.chat.completions.create(
            model=self.extractor.model,
            messages=[
                {"role": "system", "content": "你是一个专业的方案撰写助手，风格正式、客观、条理清晰..."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5  # 稍高温度保证表达多样性
        )
        
        # 3. 生成 Markdown 格式的方案文档
        result_text = response.choices[0].message.content
        
        # 确保标题正确
        if not result_text.startswith('#'):
            result_text = f"# {title}\n\n{result_text}"
        
        return result_text
```

**输出格式示例**：
```markdown
# 基于 3 个网页的方案初稿

## 一、背景

基于收集的信息，相关背景如下：

- 数字化转型已成为行业发展趋势
- 相关政策支持力度不断加大
- 技术基础设施逐步完善

## 二、现状分析

当前情况分析如下：

- 行业整体处于快速发展阶段
- 部分企业已开始数字化转型实践
- 存在技术标准和规范不统一的问题

...
```

---

## 🚀 快速开始

### 📦 安装依赖

```bash
# 克隆项目（如果有 Git 仓库）
git clone <repository-url>
cd WebToProposal

# 安装 Python 依赖
pip install -r requirements.txt
```

**依赖说明**：
- `requests`：HTTP 请求库，用于抓取网页
- `beautifulsoup4`：HTML 解析库，用于提取内容
- `openai`：OpenAI API 客户端（可选，用于 LLM 功能）
- `lxml`：XML/HTML 解析器，BeautifulSoup 的后端

### 🎯 基本使用

#### 步骤 1：准备 URL 列表文件

创建 `urls.txt` 文件，每行一个 URL：

```txt
https://www.example.com/news/tech-trends-2024
https://www.example.com/reports/industry-analysis
https://www.example.com/policy/digital-transformation
```

#### 步骤 2：运行命令

```bash
python cli.py urls.txt --out proposal.md
```

#### 步骤 3：查看生成的方案

打开 `proposal.md` 查看生成的方案初稿！

### 🤖 使用 LLM（推荐）

为了获得更好的效果，建议配置 OpenAI API：

#### 方式 1：环境变量（推荐）

```bash
# Linux/Mac
export OPENAI_API_KEY=your_api_key_here

# Windows PowerShell
$env:OPENAI_API_KEY="your_api_key_here"

# Windows CMD
set OPENAI_API_KEY=your_api_key_here
```

#### 方式 2：命令行参数

```bash
python cli.py urls.txt --out proposal.md --api-key your_api_key_here
```

#### 方式 3：使用兼容 OpenAI API 的服务

```bash
python cli.py urls.txt --out proposal.md \
    --api-key your_key \
    --base-url https://api.example.com/v1 \
    --model gpt-3.5-turbo
```

**支持的模型**：
- `gpt-3.5-turbo`（默认，性价比高）
- `gpt-4`（效果更好，但成本更高）
- 任何兼容 OpenAI API 的模型

**注意**：
- ⚠️ 如果不设置 API Key，程序会使用简化模式，功能仍然可用但效果会有所降低
- 💡 简化模式基于规则提取，适合快速测试或简单场景

---

## 📖 完整使用示例

### 输入文件 (`examples/input_urls.txt`)

```txt
# 示例 URL 列表
# 每行一个 URL，以 # 开头的行为注释

https://www.example.com/news/tech-trends-2024
https://www.example.com/reports/industry-analysis
https://www.example.com/policy/digital-transformation
```

### 运行命令

```bash
python cli.py examples/input_urls.txt --out examples/output_proposal.md --verbose
```

### 输出结果 (`examples/output_proposal.md`)

```markdown
# 基于 3 个网页的方案初稿

## 一、背景

基于收集的信息，相关背景如下：

- 数字化转型已成为行业发展趋势
- 相关政策支持力度不断加大
- 技术基础设施逐步完善
- 市场需求持续增长
- 国际竞争日趋激烈

## 二、现状分析

当前情况分析如下：

- 行业整体处于快速发展阶段
- 部分企业已开始数字化转型实践
- 存在技术标准和规范不统一的问题
- 区域发展不平衡
- 创新能力有待提升

## 三、核心问题总结

通过分析，主要问题包括：

- 缺乏统一的技术标准
- 人才储备不足
- 资金投入压力大
- 数据安全和隐私保护挑战
- 传统企业转型困难

## 四、可行方案建议

基于以上分析，建议采取以下方案：

- 建立行业技术标准体系
- 加强人才培养和引进
- 探索多元化资金支持模式
- 完善数据安全和隐私保护机制
- 提供针对性的转型指导和支持
```

---

## ⚙️ 命令行参数详解

```bash
python cli.py <input_file> [options]
```

### 必需参数

- `input`：输入文件路径（每行一个 URL）

### 可选参数

| 参数 | 说明 | 默认值 | 示例 |
|------|------|--------|------|
| `--out` | 输出文件路径 | `proposal.md` | `--out my_proposal.md` |
| `--api-key` | OpenAI API Key | 从环境变量读取 | `--api-key sk-xxx` |
| `--base-url` | API 基础 URL | OpenAI 官方 API | `--base-url https://api.example.com/v1` |
| `--model` | 使用的模型名称 | `gpt-3.5-turbo` | `--model gpt-4` |
| `--verbose` | 显示详细日志 | `False` | `--verbose` |

### 使用示例

```bash
# 基本使用
python cli.py urls.txt

# 指定输出文件
python cli.py urls.txt --out my_proposal.md

# 使用自定义 API Key 和模型
python cli.py urls.txt --api-key sk-xxx --model gpt-4

# 显示详细日志（调试用）
python cli.py urls.txt --verbose

# 使用兼容 API 服务
python cli.py urls.txt \
    --api-key your_key \
    --base-url https://api.example.com/v1 \
    --model gpt-3.5-turbo
```

---

## 🔧 工作原理深度解析

### 完整工作流程

```
输入 URL 列表
    ↓
[1] 网页抓取 (crawler.py)
    ├─ 发送 HTTP 请求
    ├─ 解析 HTML
    ├─ 提取正文内容
    └─ 过滤广告/导航
    ↓
[2] 信息提取 (extractor.py)
    ├─ LLM 智能提取（可选）
    │  ├─ 关键事实
    │  ├─ 重要论述
    │  └─ 问题描述
    └─ 简化模式（无 LLM）
    ↓
[3] 信息融合 (merger.py)
    ├─ 识别共性信息
    ├─ 去除重复内容
    ├─ 保留独特视角
    └─ 主题聚类
    ↓
[4] 方案规划 (planner.py)
    ├─ 规划背景部分
    ├─ 规划现状分析
    ├─ 规划问题总结
    └─ 规划方案建议
    ↓
[5] 方案生成 (writer.py)
    ├─ 生成正式文档
    ├─ 使用办公风格
    └─ 输出 Markdown
    ↓
方案初稿 (proposal.md)
```

### 关键技术细节

#### 1. 网页内容提取策略

**多层级内容识别**：
```python
# 优先级顺序
content_selectors = [
    'article',           # 语义化标签（最优先）
    'main',              # 主要内容区域
    '[role="main"]',     # ARIA 角色
    '.content',          # 常见类名
    '.post-content',     # 博客类名
    '.article-content',  # 文章类名
    '#content',          # ID 选择器
    '#main-content',     # 主内容 ID
    'body'               # 兜底方案
]
```

**噪音过滤**：
```python
# 移除的标签
noise_tags = [
    'script',      # JavaScript 代码
    'style',       # CSS 样式
    'nav',         # 导航栏
    'header',      # 页眉
    'footer',      # 页脚
    'aside',       # 侧边栏
    'advertisement', # 广告
    'ad',          # 广告
    'noscript'     # 无脚本内容
]
```

#### 2. LLM Prompt 设计原则

**核心原则**：
- ✅ **只提取，不编造**：所有 prompt 都强调"只基于提供的信息"
- ✅ **结构化输出**：强制 JSON 格式，便于程序处理
- ✅ **低温度设置**：temperature=0.3，保证输出稳定
- ✅ **明确角色**：system message 明确 AI 的角色和任务

**Prompt 模板结构**（`prompts.py`）：
```python
EXTRACTION_PROMPT = """
你是一个专业的信息提取助手。请从以下网页内容中提取关键信息。

网页标题：{title}
网页URL：{url}

网页内容：
{content}

请提取以下信息：
1. 关键事实：重要的事件、数据、政策、趋势等
2. 重要论述：核心观点、分析、判断等
3. 问题描述：提到的挑战、困难、问题等

输出格式（JSON）：
{{
    "key_facts": ["事实1", "事实2", ...],
    "key_arguments": ["论述1", "论述2", ...],
    "problems": ["问题1", "问题2", ...]
}}

只提取网页中明确提到的内容，不要编造或推测。
"""
```

#### 3. 信息融合算法

**融合策略**：
1. **共性识别**：找出多个网页都提到的相同或相似内容
2. **去重处理**：合并重复的信息点
3. **视角保留**：保留不同来源的独特观点
4. **主题聚类**：将信息按主题分类

**示例**：
```
网页1: "数字化转型是趋势" + "需要统一标准"
网页2: "数字化转型是趋势" + "人才短缺"
网页3: "数字化转型是趋势" + "资金压力大"

融合结果:
- 共性: "数字化转型是趋势"（三个网页都提到）
- 独特: ["需要统一标准", "人才短缺", "资金压力大"]
```

#### 4. 容错机制

**多级降级策略**：
1. **LLM 模式**：使用 GPT 等模型，效果最好
2. **简化模式**：无 LLM 时，基于规则提取
3. **错误处理**：每个模块都有 try-except，保证程序不崩溃

**示例代码**：
```python
def extract(self, page_data: Dict[str, str]) -> Dict[str, Any]:
    if not self.client:
        # 降级到简化模式
        return self._simple_extract(page_data)
    
    try:
        # 尝试使用 LLM
        response = self.client.chat.completions.create(...)
        return result
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        # 降级到简化模式
        return self._simple_extract(page_data)
```

---

## 📁 项目结构详解

```
webtoproposal/
├── README.md                    # 📖 项目文档（本文件）
├── requirements.txt             # 📦 Python 依赖列表
├── cli.py                       # 🚀 命令行入口
│
├── webtoproposal/              # 📂 核心模块包
│   ├── __init__.py             # 📝 包初始化文件
│   │
│   ├── crawler.py              # 🕷️ 网页抓取与清洗
│   │   └── WebCrawler          # 爬虫类：抓取网页、提取正文
│   │
│   ├── extractor.py            # 🔍 关键信息抽取
│   │   └── InformationExtractor # 抽取器：从网页中提取结构化信息
│   │
│   ├── merger.py               # 🔀 多网页信息融合
│   │   └── InformationMerger   # 融合器：合并、去重、聚类
│   │
│   ├── planner.py              # 📐 方案结构规划
│   │   └── ProposalPlanner     # 规划器：规划方案结构
│   │
│   ├── writer.py               # ✍️ 方案文本生成
│   │   └── ProposalWriter      # 撰写器：生成最终方案文档
│   │
│   ├── prompts.py              # 💬 LLM Prompt 模板
│   │   ├── EXTRACTION_PROMPT   # 信息提取 Prompt
│   │   ├── MERGE_PROMPT        # 信息融合 Prompt
│   │   ├── PLANNING_PROMPT     # 方案规划 Prompt
│   │   └── WRITING_PROMPT      # 方案撰写 Prompt
│   │
│   └── utils.py                # 🛠️ 工具函数
│       ├── setup_logging       # 日志配置
│       ├── clean_text          # 文本清理
│       ├── chunk_text          # 文本分块
│       └── validate_url        # URL 验证
│
└── examples/                   # 📚 示例文件
    ├── input_urls.txt          # 输入示例（URL 列表）
    └── output_proposal.md      # 输出示例（方案文档）
```

### 模块职责说明

| 模块 | 职责 | 输入 | 输出 |
|------|------|------|------|
| `crawler.py` | 网页抓取 | URL | 网页标题和正文 |
| `extractor.py` | 信息提取 | 网页内容 | 结构化信息（事实、论述、问题） |
| `merger.py` | 信息融合 | 多个网页的结构化信息 | 融合后的信息（共性、独特、主题） |
| `planner.py` | 方案规划 | 融合后的信息 | 方案结构规划（四部分） |
| `writer.py` | 方案生成 | 方案结构规划 | 最终方案文档（Markdown） |

---

## 🎯 核心功能详解

### 1. 智能网页抓取 🔍

**功能特点**：
- ✅ 自动识别网页编码，避免乱码
- ✅ 智能提取正文内容，过滤广告和导航
- ✅ 支持多种内容容器（article、main、.content 等）
- ✅ 保留标题层级结构（h1-h6）
- ✅ 自定义 User-Agent，避免被反爬

**技术实现**：
```python
# 编码自动识别
response.encoding = response.apparent_encoding or 'utf-8'

# 噪音标签移除
for tag in soup(['script', 'style', 'nav', 'header', 'footer']):
    tag.decompose()

# 多层级内容查找
content_selectors = ['article', 'main', '[role="main"]', '.content', 'body']
```

### 2. 信息抽取 🧠

**功能特点**：
- ✅ LLM 智能提取（支持 GPT-3.5/4 等）
- ✅ 无 LLM 时自动降级到简化模式
- ✅ 提取关键事实、重要论述、问题描述
- ✅ 强制 JSON 格式输出，便于处理

**提取内容类型**：
- 📌 **关键事实**：重要的事件、数据、政策、趋势等
- 💭 **重要论述**：核心观点、分析、判断等
- ⚠️ **问题描述**：提到的挑战、困难、问题等

### 3. 信息融合 🔀

**功能特点**：
- ✅ 自动识别共性信息（多个网页都提到的内容）
- ✅ 智能去重，避免重复内容
- ✅ 保留独特视角（不同来源的独特观点）
- ✅ 主题聚类，便于后续规划

**融合策略**：
```
输入：3 个网页的提取信息
  ↓
识别共性：找出 3 个网页都提到的内容
  ↓
去重处理：合并重复的信息点
  ↓
保留独特：保留不同来源的独特观点
  ↓
主题聚类：按主题分类归纳
  ↓
输出：融合后的信息（共性 + 独特 + 主题）
```

### 4. 方案规划 📐

**功能特点**：
- ✅ 固定输出结构（四部分）
- ✅ 基于融合信息规划，不编造内容
- ✅ 每部分包含要点和分析

**输出结构**：
1. **背景 (Background)**
   - 主要要点
   - 关键事实

2. **现状分析 (Current Situation)**
   - 主要要点
   - 分析内容

3. **核心问题总结 (Key Problems)**
   - 问题列表
   - 影响分析

4. **可行方案建议 (Proposed Solutions)**
   - 方案列表
   - 理由说明

### 5. 方案生成 ✍️

**功能特点**：
- ✅ 正式、客观的办公文档风格
- ✅ 段落 + 条列结合
- ✅ Markdown 格式输出
- ✅ 可直接修改使用

**文档风格**：
- 📄 客观、条理清晰
- 📝 适合办公场景使用
- 🎯 语言简洁、准确
- ✏️ 可直接修改使用

---

## ⚠️ 重要说明

### 🎯 设计原则

1. **这是整理工具，不是生成工具**
   - ✅ 所有内容基于输入的网页信息
   - ❌ 不编造事实
   - ❌ 不引入网页之外的新信息

2. **需要人工审核**
   - ✅ 生成的方案是初稿
   - ✅ 需要人工审核和修改
   - ✅ 建议根据实际情况调整

3. **不替代决策**
   - ✅ 工具只负责整理信息
   - ❌ 不替代人工决策
   - ❌ 不提供决策建议

### 🔒 使用限制

- ⚠️ **网页可访问性**：只能抓取公开可访问的网页
- ⚠️ **反爬虫机制**：部分网站可能有反爬虫机制，可能无法抓取
- ⚠️ **内容质量**：输出质量取决于输入网页的内容质量
- ⚠️ **LLM 成本**：使用 LLM 会产生 API 调用费用

### 💡 最佳实践

1. **URL 选择**
   - ✅ 选择高质量、权威的网页
   - ✅ 确保网页内容与主题相关
   - ✅ 建议 3-10 个 URL，不要太多或太少

2. **API Key 配置**
   - ✅ 使用环境变量存储 API Key（更安全）
   - ✅ 定期检查 API 使用量
   - ✅ 选择合适的模型（gpt-3.5-turbo 性价比高）

3. **结果处理**
   - ✅ 仔细审核生成的方案
   - ✅ 根据实际情况调整内容
   - ✅ 补充必要的细节和数据

---

## 🛠️ 开发说明

### 🔧 扩展性设计

**模块化架构**：
- 各模块独立，易于替换和扩展
- 接口清晰，便于测试和维护

**Prompt 集中管理**：
- 所有 LLM prompt 集中在 `prompts.py`
- 便于调整风格和优化效果

**容错机制**：
- 支持无 LLM 的简化模式
- 保证基本功能可用

### 📝 代码规范

- **类型提示**：使用 Python 类型提示，提高代码可读性
- **文档字符串**：所有函数都有详细的文档字符串
- **日志记录**：使用 logging 模块记录关键操作
- **错误处理**：完善的异常处理机制

### 🧪 测试建议

```python
# 单元测试示例
def test_crawler():
    crawler = WebCrawler()
    result = crawler.fetch("https://example.com")
    assert result is not None
    assert 'title' in result
    assert 'content' in result

# 集成测试示例
def test_full_pipeline():
    # 测试完整流程
    pass
```

### 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

**贡献方向**：
- 🐛 Bug 修复
- ✨ 新功能开发
- 📖 文档改进
- 🎨 代码优化

---

## 📊 性能优化建议

### 🚀 提升处理速度

1. **并发抓取**：使用多线程/异步抓取多个网页
2. **缓存机制**：缓存已抓取的网页内容
3. **批量处理**：批量调用 LLM API

### 💰 降低 API 成本

1. **选择合适的模型**：gpt-3.5-turbo 性价比高
2. **内容截断**：限制输入长度，避免超出 token 限制
3. **简化模式**：无 LLM 时使用简化模式

### 📈 提升输出质量

1. **优化 Prompt**：根据实际效果调整 prompt
2. **后处理**：对 LLM 输出进行后处理和验证
3. **人工反馈**：收集用户反馈，持续优化

---

## 📚 相关资源

### 🔗 相关项目

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - HTML 解析库
- [OpenAI API](https://platform.openai.com/docs) - OpenAI API 文档
- [Requests](https://requests.readthedocs.io/) - HTTP 库

### 📖 学习资源

- [Python 爬虫教程](https://docs.python.org/3/)
- [LLM Prompt 工程](https://platform.openai.com/docs/guides/prompt-engineering)
- [Markdown 语法](https://www.markdownguide.org)

---

## 🧩 常见问题（FAQ）

### 1) 生成内容会不会“瞎编”？

**设计目标是不瞎编**：本项目的 LLM 仅用于**总结 / 结构化 / 表达重组**，并在 `prompts.py` 中明确强调“只基于提供内容，不要引入网页之外信息”。  
但现实里任何 LLM 都可能出现偏差，因此依然需要你在提交前进行人工复核 ✅

### 2) 为什么我抓取到的内容很少 / 为空？

可能原因：
- 🔒 **网站有反爬**：需要登录、需要 JS 渲染、或对 UA/频率敏感
- 🧱 **页面主要内容由 JS 动态生成**：`requests + BeautifulSoup` 只能拿到初始 HTML
- 🧩 **正文容器不在常见选择器里**：例如内容在更深层的自定义标签中

排查建议：
- 用浏览器打开 URL，右键“查看源代码”，确认正文是否在源代码里
- 先用少量网页验证流程（建议 3 个 URL）
- 对目标网站可在 `crawler.py` 增加更贴合的选择器（如站点特定的 `.articleBody` / `#js_content` 等）

### 3) 为什么输出重复很多、像拼接？

建议：
- ✅ 使用 LLM 模式（配置 `OPENAI_API_KEY`），融合阶段 `merger.py` 会更强
- ✅ 输入 URL 不要过多且尽量“来源互补”（政策 + 报告 + 新闻 + 官方解读）
- ✅ 对内容极相似的网页（转载、镜像）尽量不要重复输入

### 4) 如何让输出更“像能交上去的方案”？

你可以从三处入手：
- **输入更干净**：尽量选择正文清晰、结构良好的页面
- **Prompt 调优**：在 `webtoproposal/prompts.py` 中调整措辞和输出约束
- **写作风格固化**：在 `WRITING_PROMPT` 中增加你们组织的“模板口吻/术语/格式规范”

---

## 🎛️ Prompt 调优指南（写得更像办公文档）

`webtoproposal/prompts.py` 是风格与约束的“总开关”：

- **想更客观**：在 `WRITING_PROMPT` 里加入“避免主观判断、避免夸张形容词、避免营销话术”
- **想更结构化**：要求每节都输出“段落 + 条列”，并强制条列以动宾短语开头（例如“建立…、完善…、推动…”）
- **想更可审核**：要求每个要点后追加“来源提示”（例如“来源：网页1/网页2”）

你可以把下述约束追加到 `WRITING_PROMPT`（示例）：

```text
补充要求：
1) 每条要点尽量写成可执行动作（动词开头）
2) 避免口号化表述，尽量落到机制/流程/职责/指标
3) 如果信息不足，用“（待补充）”占位，不要自行补全
```

---

## 🧯 排错与调试

### 开启详细日志

```bash
python cli.py urls.txt --out proposal.md --verbose
```

### Windows PowerShell 设置环境变量

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
python cli.py urls.txt --out proposal.md
```

### 常见报错原因速查

- **`Invalid URL`**：URL 格式不符合 `http(s)://...`，检查是否缺少协议头
- **抓取超时**：网络不通/站点慢/被限制，可在 `crawler.py` 增加超时或重试
- **LLM 调用失败**：API Key 未配置、网络问题、base_url 不正确、模型名不可用

---

## 🗺️ Roadmap（后续可演进方向）

如果你准备把它做成“真办公刚需”，建议优先演进这些方向：

- 🚄 **并发抓取**：多线程/异步抓取，显著提升速度
- 🧠 **更强的正文抽取**：加入更成熟的正文提取策略（站点适配、可读性算法等）
- 🧾 **引用与可追溯**：每个要点带来源 URL/段落索引，方便核对与审计
- 🧱 **输出模板体系**：支持“申报书/调研报告/商业方案”不同固定模板
- 🧩 **本地缓存**：避免重复抓取和重复 LLM 花费
- 🔎 **信息可信度分级**：按来源权威性/发布日期/是否多源一致进行标注

---

## 🙏 致谢（Acknowledgements）

- `requests`：稳定好用的 HTTP 客户端
- `BeautifulSoup4` / `lxml`：HTML 解析与文本提取
- `openai` SDK：调用兼容 OpenAI API 的大模型服务

---

## ✅ 最后一句（真的很重要）

这个工具的定位是：**把“搜集 + 整理 + 结构化”自动化**，让你把时间花在更高价值的事上：
- **做判断**（要不要做、怎么做）
- **做取舍**（路线、边界、资源）
- **做落地**（指标、计划、预算、风险）


它不会替你做决策，但会让你更快进入决策阶段。🚀

---

## 👤 作者 (Author)

**Haoze Zheng**

*   🎓 **School**: Xinjiang University (XJU)
*   📧 **Email**: zhenghaoze@stu.xju.edu.cn
*   🐱 **GitHub**: [mire403](https://github.com/mire403)

---

<div align="center">

**如果这个项目对你有帮助，请给个 ⭐ Star！**

<sub>Made by Haoze Zheng. 2026 WebToProposal.</sub>

</div>




