# Markdown 转 HTML 转换器

一个通用的 OpenClaw 技能，用于将 Markdown 文件转换为 HTML，支持 GitHub 风格 Markdown。

## 功能特性

- ✅ GitHub 风格 Markdown 支持
- ✅ 表格渲染
- ✅ 代码语法高亮
- ✅ 自动生成目录
- ✅ 自定义 CSS 支持
- ✅ 响应式设计

## 安装

```bash
# 从 skillhub 安装
skillhub install markdown-to-html

# 或手动克隆
git clone https://github.com/yikexiaoyao/markdown-to-html.git
```

## 使用方法

### 命令行

```bash
# 基本转换
python3 md2html.py input.md -o output.html

# 使用自定义 CSS
python3 md2html.py input.md -o output.html --css style.css
```

### 作为模块使用

```python
from md2html import convert_markdown

html = convert_markdown('# 你好世界')
```

## 配置

创建 `config.json` 自定义配置：

```json
{
  "defaultCss": true,
  "highlightCode": true,
  "generateToc": true,
  "outputDir": "./output"
}
```

## 依赖

- Python 3.6+
- markdown 库

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 作者

OpenClaw Community