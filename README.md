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
# 手动克隆
git clone https://github.com/yikexiaoyao/markdown-to-html.git
cd markdown-to-html
```

## 使用方法

### 命令行

```bash
# 基本转换
python3 md2html.py input.md -o output.html

# 使用自定义 CSS
python3 md2html.py input.md -o output.html --css style.css

# 查看帮助
python3 md2html.py --help
```

### Python 调用

```python
import subprocess

# 调用转换脚本
subprocess.run([
    'python3', 'md2html.py', 
    'input.md', 
    '-o', 'output.html'
])
```

## 依赖

- Python 3.6+
- markdown 库

安装依赖：
```bash
pip install markdown
```

## 输出示例

转换后的 HTML 包含：
- 响应式布局（最大宽度 900px）
- GitHub 风格样式
- 代码高亮
- 表格样式

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 作者

OpenClaw Community