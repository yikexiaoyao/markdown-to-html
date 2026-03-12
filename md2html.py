#!/usr/bin/env python3
"""Markdown to HTML converter using markdown library."""

import sys
import argparse
import markdown
from pathlib import Path

# Default CSS style
DEFAULT_CSS = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
    background: #fff;
}
h1, h2, h3, h4, h5, h6 {
    color: #2c3e50;
    margin-top: 24px;
    margin-bottom: 16px;
}
code {
    background: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
}
pre {
    background: #f8f8f8;
    padding: 16px;
    border-radius: 6px;
    overflow-x: auto;
}
pre code {
    background: none;
    padding: 0;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 16px 0;
}
th, td {
    border: 1px solid #ddd;
    padding: 8px 12px;
    text-align: left;
}
th {
    background: #f5f5f5;
    font-weight: 600;
}
blockquote {
    border-left: 4px solid #ddd;
    margin: 0;
    padding-left: 16px;
    color: #666;
}
a {
    color: #0366d6;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
img {
    max-width: 100%;
    height: auto;
}
</style>
</head>
<body>
"""

FOOTER = """
</body>
</html>
"""

def convert_markdown_to_html(input_file, output_file=None, css_file=None):
    """Convert markdown file to HTML."""
    input_path = Path(input_file)
    
    if not input_path.exists():
        print(f"Error: File not found: {input_file}", file=sys.stderr)
        sys.exit(1)
    
    # Read markdown content
    md_content = input_path.read_text(encoding='utf-8')
    
    # Convert to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=[
            'markdown.extensions.tables',
            'markdown.extensions.fenced_code',
            'markdown.extensions.toc',
            'markdown.extensions.nl2br',
        ]
    )
    
    # Build full HTML
    if css_file and Path(css_file).exists():
        css_content = Path(css_file).read_text(encoding='utf-8')
        full_html = f"<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"UTF-8\">\n<style>\n{css_content}\n</style>\n</head>\n<body>\n{html_content}\n</body>\n</html>"
    else:
        full_html = DEFAULT_CSS + html_content + FOOTER
    
    # Write output
    if output_file:
        output_path = Path(output_file)
        output_path.write_text(full_html, encoding='utf-8')
        print(f"✅ Converted: {input_file} → {output_file}")
    else:
        print(full_html)

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to HTML')
    parser.add_argument('input', help='Input markdown file')
    parser.add_argument('-o', '--output', help='Output HTML file')
    parser.add_argument('--css', help='Custom CSS file')
    
    args = parser.parse_args()
    
    convert_markdown_to_html(args.input, args.output, args.css)

if __name__ == '__main__':
    main()