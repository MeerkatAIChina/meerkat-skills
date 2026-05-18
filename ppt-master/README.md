# PPT Master — 快速开始

> AI 生成原生可编辑 PPTX。输入 PDF/DOCX/URL/Markdown → 输出 PowerPoint。

## 安装

```bash
git clone https://github.com/hugohe3/ppt-master.git
cd ppt-master
pip install -r requirements.txt
```

## 使用

在 AI IDE（Claude Code / Cursor / VS Code Copilot）中输入：

```
请帮我做一份关于 Q3 业绩的 PPT，源文件是 report.pdf
```

AI 自动执行 7 步链路，生成可编辑 `.pptx`。

## 关键命令

```bash
# 初始化项目
python3 scripts/project_manager.py init my-deck --format ppt169

# 导入源文件
python3 scripts/project_manager.py import-sources my-deck report.pdf --move

# 导出 PPTX（Step 7 三步串行）
python3 scripts/total_md_split.py my-deck
python3 scripts/finalize_svg.py my-deck
python3 scripts/svg_to_pptx.py my-deck -s final
```

## 文档

- 完整工作流：`SKILL.md`
- 技术规范：`references/shared-standards.md`
- FAQ：`docs/faq.md`

## 依赖

- Python 3.10+
- pip packages：`requirements.txt`
- 可选：Node.js 18+（微信页面）、Pandoc（遗留格式）

---

*Version: 2.7.0 | MIT License | Source: hugohe3/ppt-master*
