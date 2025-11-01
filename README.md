# terminalcode - Terminal-Style Code Boxes for LaTeX

A modern LaTeX package providing terminal-style code display with UTF-8 box-drawing characters, ANSI 16-color support, and dark/light themes.

*This package was developed with AI assistance for rapid prototyping and comprehensive documentation.*

**Version**: 0.9.0 | **Date**: 2025-11-02 | **License**: MIT | **CTAN Status**: Ready

## 📦 Package Info

| Field | Value |
|-------|-------|
| **Name** | `terminalcode` |
| **Version** | 0.9.0 |
| **License** | MIT |
| **Author** | LoveElysia1314 |
| **Contact** | dr.zqr@outlook.com |
| **Repository** | [GitHub](https://github.com/LoveElysia1314/terminalcode-sty) |

## 🚀 Quick Start

```latex
\documentclass{article}
\usepackage{terminalcode}  % dark theme (default)

\begin{document}

\begin{termcode}[bash]{Terminal Session}
$ echo "Hello, World!"
Hello, World!
$ python --version
Python 3.9.0
\end{termcode}

\end{document}
```

**Compile with:** `xelatex document.tex` or `lualatex document.tex`

## ✨ Features

- **Terminal-style code boxes** with authentic styling
- **ANSI 16-color support** (dark/light themes)
- **Theme switching** - `\terminalcodetheme{light}`
- **Multi-language** - bash, python, text, etc.
- **External file inclusion** - `\terminput{Title}{file}`
- **UTF-8 box-drawing** characters
- **Line numbers** & automatic wrapping
- **LaTeX escape** via `«»` delimiters

## 📋 Requirements

### Required Compilers
- ✅ **XeLaTeX** (recommended)
- ✅ **LuaLaTeX**
- ❌ **pdfLaTeX** (not supported)

### Required Packages
- `xcolor`, `tcolorbox` (with `most`), `listings`, `fontspec`, `kvoptions`

### Fonts (with fallback)
1. **Primary**: DejaVu Sans Mono
2. **Fallback**: Latin Modern Mono
3. **System default** (with warning)

## 🔧 Installation

### Local Installation
```latex
% Place terminalcode.sty in project directory
\usepackage{terminalcode}
```

### System Installation
**Linux/macOS:**
```bash
mkdir -p ~/texmf/tex/latex/terminalcode
cp terminalcode.sty ~/texmf/tex/latex/terminalcode/
mktexlsr
```

**Windows (MiKTeX):**
```cmd
copy terminalcode.sty "C:\Program Files\MiKTeX\tex\latex\terminalcode\"
initexmf --update-fndb
```

## 🎯 Usage Examples

### Basic with Options
```latex
\usepackage[theme=light,monofont=Consolas]{terminalcode}
```

### Theme Switching
```latex
\usepackage{terminalcode}

% Dark theme (default)
\begin{termcode}[text]{Dark Mode}
content
\end{termcode}

% Switch to light
\terminalcodetheme{light}

\begin{termcode}[text]{Light Mode} 
content
\end{termcode}
```

### External Files
```latex
\terminput[python]{Data Script}{scripts/process.py}
% Alias:
\termcodefileinput[bash]{Deploy Script}{deploy.sh}
```

### ANSI Colors in Code
```latex
\begin{termcode}[text]{Colored Output}
Normal «\ac{31}»Red Text«\ansireset» Normal
«\ac{92}»Bright Green«\ansireset» Normal
\end{termcode}
```

## 📖 API Reference

### Environments

| Command | Parameters | Description |
|---------|------------|-------------|
| `termcode[lang]{title}` | `lang`: language (default: text)<br>`title`: box title | Main code environment |

### Commands

| Command | Parameters | Description |
|---------|------------|-------------|
| `\terminalcodetheme{theme}` | `dark` or `light` | Switch theme |
| `\terminput[lang]{title}{file}` | `lang`: language<br>`title`: box title<br>`file`: filename | Include external file |
| `\ansicolor{color}` | `color`: ANSI code (30-37, 90-97) | Apply ANSI color |
| `\ansireset` | - | Reset formatting |

**Aliases:** `\tctheme`, `\termcodefileinput`, `\ac`

### Package Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `theme` | `dark`, `light` | `dark` | Initial theme |
| `monofont` | Font name | `DejaVu Sans Mono` | Monospace font |

## 🎨 ANSI Colors

### Standard Colors (30-37)

| Code | Color | Dark Theme | Light Theme |
|------|-------|------------|-------------|
| 30 | Black | (46,52,54) | (127,140,141) |
| 31 | Red | (205,75,69) | (200,55,47) |
| 32 | Green | (75,183,72) | (39,174,96) |
| 33 | Yellow | (218,165,32) | (214,147,40) |
| 34 | Blue | (72,120,200) | (52,152,219) |
| 35 | Magenta | (164,84,208) | (142,68,173) |
| 36 | Cyan | (55,180,180) | (26,188,156) |
| 37 | White | (230,230,230) | (230,230,230) |

**Bright colors** available with codes 90-97.

## ⚠️ Troubleshooting

### Common Issues

**"Requires XeLaTeX or LuaLaTeX"**
- **Problem**: Using pdfLaTeX
- **Fix**: Compile with `xelatex` or `lualatex`

**Font warnings**
- **Problem**: Requested font not found
- **Fix**: Install font or use different `monofont` option

**Unicode characters not displaying**
- **Problem**: UTF-8 encoding issues
- **Fix**: Ensure UTF-8 file encoding and use XeLaTeX

## 📄 Version History

### v0.9.0 (2025-11-02) - Initial Release
- Terminal-style code boxes with ANSI colors
- Dark/light theme support
- External file inclusion
- Font fallback mechanism
- CTAN-ready structure

## 📜 License

MIT License - See LICENSE file for details.

## 🤝 Contributing

Bug reports and feature requests welcome via [GitHub Issues](https://github.com/LoveElysia1314/terminalcode-sty/issues).

---

**Repository**: [github.com/LoveElysia1314/terminalcode-sty](https://github.com/LoveElysia1314/terminalcode-sty)  
**CTAN**: [ctan.org/pkg/terminalcode](https://ctan.org/pkg/terminalcode)