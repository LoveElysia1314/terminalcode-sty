# Changelog

All notable changes to the `terminalcode` package will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.9.0] - 2025-11-02

**Initial Release — Ready for CTAN**

*This package and project were primarily developed using AI assistance.*

### Added

- ✨ **Terminal-Style Code Display** — Authentic terminal-appearance code boxes with UTF-8 box-drawing characters and ANSI colors
- ✨ **`termcode` Environment** — Display code inline with language-specific syntax highlighting (bash, python, text, etc.)
- ✨ **`\terminput` / `\termcodefileinput` Commands** — Embed code from external files with terminal styling
- ✨ **ANSI 16-Color Palette** — Standard (30-37) and bright (90-97) color codes with dark/light theme variants
- ✨ **Theme System** — Dynamic theme switching via `\terminalcodetheme{dark|light}` 
  - Dark theme: Terminal-like dark background
  - Light theme: Light background with readable contrast
- ✨ **Package Options** — Configure at load time:
  - `theme=dark|light` — initial theme (default: `dark`)
  - `monofont=<fontname>` — custom monospace font (default: `DejaVu Sans Mono`)
- ✨ **Engine Detection & Validation** — Automatic XeLaTeX/LuaLaTeX detection with clear error messages for pdfLaTeX
- ✨ **Font Fallback Mechanism** — Graceful degradation: DejaVu Sans Mono → Latin Modern Mono → system default
- ✨ **LaTeX Escape Sequences** — Use `«` and `»` delimiters to inject LaTeX commands within code
- ✨ **Automatic Line Numbers** — Left-side numbering with customizable styling
- ✨ **Line Breaking** — Automatic word wrapping for long lines with breakable boxes across pages
- ✨ **Comprehensive Documentation**:
  - Full README with installation, quick start, API reference, troubleshooting
  - 6-page PDF documentation (`terminalcode-doc.tex`)
  - Working example file (`example.tex`) demonstrating all features
  - Build scripts for CTAN submission (`mkctan.bat`, `mkctan.sh`)

### Technical Specifications

**Core Requirements:**
- **TeX Compiler**: XeLaTeX (recommended) or LuaLaTeX — **NOT pdfLaTeX**
- **Required Packages**: `xcolor`, `tcolorbox` (with `most` option), `listings`, `fontspec`, `kvoptions`
- **System Fonts**: DejaVu Sans Mono or Latin Modern Mono
- **File Encoding**: UTF-8

**Supported Platforms:**
- ✅ Linux/Unix with TeX Live 2020+
- ✅ macOS with MacTeX
- ✅ Windows with MiKTeX or TeX Live
- ✅ Overleaf (online LaTeX editor)

---

## Roadmap (Planned for Future Releases)

- [ ] Support for 256-color and 24-bit (true color) ANSI codes
- [ ] Automatic ANSI sequence parsing from terminal output
- [ ] Package option for customizing escape delimiters
- [ ] Line number styling and color customization
- [ ] User-defined style hooks for extensibility
- [ ] Integration with `minted` package for advanced syntax highlighting
- [ ] Additional theme variants (solarized, monokai, etc.)
- [ ] GitHub Actions CI/CD workflow for automated testing and PDF generation

## Known Limitations

- Line numbers may not display in certain `tcolorbox` configurations (cosmetic issue, does not affect functionality)
- Very long lines with special characters may cause word-wrapping issues in rare edge cases
- Escape sequences (`«»`) do not work inside listings syntax-highlighted keywords (use `text` language as workaround)

## Compatibility

- **XeLaTeX**: Full support (recommended)
- **LuaLaTeX**: Full support
- **pdfLaTeX**: Not supported (requires `fontspec` and UTF-8 support)
- **Overleaf**: Compatible (has XeLaTeX available)
- **MiKTeX**: Supported (TeX Live 2020+)
- **TeX Live**: Supported (2020+)

## Support & Contributing

**Bug Reports & Feature Requests:**
- GitHub Issues: [terminalcode-sty/issues](https://github.com/LoveElysia1314/terminalcode-sty/issues)
- Documentation: [README.md#troubleshooting](README.md#troubleshooting)

**Contributing:**
- Contributions welcome! Fork the repository and submit pull requests
- Code should follow the existing style and include documentation updates

## Development Notes

**AI-Assisted Development:**

This package and project were primarily developed using AI assistance. The entire development lifecycle includes:
- Package design and architecture
- LaTeX code implementation and optimization
- Documentation writing and formatting
- Test case creation and validation
- Build script development
- CTAN compliance preparation

The AI-assisted approach has allowed for rapid prototyping, comprehensive documentation, and thorough testing while maintaining code quality and best practices.

## License

MIT License — See [LICENSE](LICENSE) file for details.

---

**For CTAN:** This package is released under the MIT License and submitted to CTAN for general distribution.

**Repository:** https://github.com/LoveElysia1314/terminalcode-sty  
**Author:** LoveElysia1314 (dr.zqr@outlook.com)  
**First Release:** 2025-11-02
