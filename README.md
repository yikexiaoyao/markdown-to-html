# Markdown to HTML Converter

A universal skill for converting Markdown files to HTML with GitHub Flavored Markdown support.

## Features

- ✅ GitHub Flavored Markdown support
- ✅ Table rendering
- ✅ Code syntax highlighting
- ✅ Auto-generated table of contents
- ✅ Custom CSS support
- ✅ Responsive design

## Installation

```bash
# From skillhub
skillhub install markdown-to-html

# Or clone manually
git clone https://github.com/yikexiaoyao/markdown-to-html.git
```

## Usage

### Command Line

```bash
# Basic conversion
python3 md2html.py input.md -o output.html

# With custom CSS
python3 md2html.py input.md -o output.html --css style.css

# Convert and preview
python3 md2html.py input.md --open
```

### As a Module

```javascript
import { convertMarkdown } from './src/convert.js';

const html = await convertMarkdown('# Hello World');
```

## Configuration

Create `config.json` to customize:

```json
{
  "defaultCss": true,
  "highlightCode": true,
  "generateToc": true,
  "outputDir": "./output"
}
```

## License

MIT