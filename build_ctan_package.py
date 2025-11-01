#!/usr/bin/env python3
"""
Build CTAN package for terminalcode LaTeX package.

This script creates a CTAN-compliant zip archive with flat structure.
Works on Windows, macOS, and Linux.

Usage:
    python build_ctan_package.py
    python build_ctan_package.py --output terminalcode.zip
    python build_ctan_package.py --help
"""

import os
import sys
import shutil
import zipfile
import argparse
from pathlib import Path

# Fix encoding for Windows terminals
if sys.platform == "win32":
    try:
        # Try to set UTF-8 output encoding
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, RuntimeError):
        pass

# File types considered text for line-ending normalization (LF)
TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".sty",
    ".tex",
    ".dtx",
    ".ins",
    ".cfg",
    ".cls",
}


def is_text_file(path: Path) -> bool:
    """Heuristic: use extension to decide if a file is text for EOL normalization."""
    ext = path.suffix.lower()
    return ext in TEXT_EXTENSIONS


def normalize_line_endings_to_lf(path: Path) -> bool:
    """Normalize a file's line endings to LF. Returns True if changed, False otherwise.

    Operates in binary mode to preserve encoding and only changes CRLF/CR to LF.
    Skips files that look binary or are not in TEXT_EXTENSIONS.
    """
    if not is_text_file(path):
        return False

    try:
        data = path.read_bytes()
    except Exception:
        return False

    # Quick binary check: presence of NUL byte
    if b"\x00" in data:
        return False

    new_data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    if new_data != data:
        path.write_bytes(new_data)
        return True
    return False


def get_project_root():
    """Get the project root directory (where this script is located)."""
    return Path(__file__).parent.resolve()


def ensure_dir(path):
    """Ensure a directory exists."""
    path.mkdir(parents=True, exist_ok=True)


def copy_file(src, dest, description=""):
    """Copy a file with error handling."""
    src_path = Path(src)
    dest_path = Path(dest)

    if not src_path.exists():
        print(f"  [!] Warning: {src} not found (skipping)")
        return False

    ensure_dir(dest_path.parent)
    shutil.copy2(src_path, dest_path)
    if description:
        print(f"  [+] {description}")
    return True


def copy_tree(src, dest, description=""):
    """Copy a directory tree with error handling."""
    src_path = Path(src)
    dest_path = Path(dest)

    if not src_path.exists():
        print(f"  [!] Warning: {src} not found (skipping)")
        return False

    if dest_path.exists():
        shutil.rmtree(dest_path)

    shutil.copytree(src_path, dest_path)
    if description:
        print(f"  [+] {description}")
    return True


def create_zip(source_dir, output_zip):
    """Create a zip archive from a directory."""
    source_path = Path(source_dir)
    output_path = Path(output_zip)

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_path):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(source_path.parent)
                zipf.write(file_path, arcname)

    return output_path.stat().st_size


def main():
    parser = argparse.ArgumentParser(
        description="Build CTAN package for terminalcode LaTeX package",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python build_ctan_package.py              # Create terminalcode.zip
  python build_ctan_package.py -o pkg.zip   # Custom output filename
  python build_ctan_package.py --verbose    # Show detailed output
        """,
    )
    parser.add_argument(
        "-o",
        "--output",
        default="terminalcode.zip",
        help="Output zip filename (default: terminalcode.zip)",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Show detailed output"
    )
    parser.add_argument(
        "--keep-temp",
        action="store_true",
        help="Keep temporary package directory after building",
    )

    args = parser.parse_args()

    # Setup paths
    root_dir = get_project_root()
    pkg_name = "terminalcode"
    pkg_dir = root_dir / pkg_name  # Flat structure directory
    output_zip = root_dir / args.output

    print("\n" + "=" * 60)
    print(f"Building CTAN Package: {pkg_name}")
    print("=" * 60 + "\n")

    try:
        # Step 1: Clean up old files
        print("Step 1: Cleaning up...")
        if pkg_dir.exists():
            shutil.rmtree(pkg_dir)
            print(f"  [+] Removed old package directory")

        if output_zip.exists():
            output_zip.unlink()
            print(f"  [+] Removed old zip file")

        # Step 2: Create package directory (flat structure)
        print("\nStep 2: Creating package directory...")
        ensure_dir(pkg_dir)
        print(f"  [+] Created {pkg_name}/ directory")

        # Step 3: Copy package file (.sty)
        print("\nStep 3: Copying package file...")

        # Try to find .sty file in root or tex/ subdirectory
        sty_file = root_dir / f"{pkg_name}.sty"
        if not sty_file.exists():
            sty_file = root_dir / "tex" / "latex" / pkg_name / f"{pkg_name}.sty"

        if not copy_file(
            sty_file, pkg_dir / f"{pkg_name}.sty", f"Copied {pkg_name}.sty"
        ):
            raise FileNotFoundError(f"Could not find {pkg_name}.sty")

        # Step 4: Copy documentation files (PDF only, not source)
        print("\nStep 4: Copying documentation...")

        # Find and copy PDF documentation
        doc_pdf = root_dir / f"{pkg_name}-doc.pdf"
        if not doc_pdf.exists():
            doc_pdf = root_dir / "doc" / "latex" / pkg_name / f"{pkg_name}-doc.pdf"

        copy_file(
            doc_pdf, pkg_dir / f"{pkg_name}-doc.pdf", f"Copied {pkg_name}-doc.pdf"
        )

        # Step 5: Copy metadata files
        print("\nStep 5: Copying metadata files...")

        # Only copy files that exist (README.md, LICENSE, CHANGELOG.md)
        for fname in ["README.md", "LICENSE", "CHANGELOG.md"]:
            src_file = root_dir / fname
            if src_file.exists():
                copy_file(src_file, pkg_dir / fname, f"Copied {fname}")

        # Step 5.5: Normalize line endings to LF in all text files
        print("\nStep 5.5: Normalizing line endings (CRLF -> LF) ...")
        changed = 0
        for f in pkg_dir.iterdir():
            if f.is_file() and is_text_file(f):
                if normalize_line_endings_to_lf(f):
                    changed += 1
                    if args.verbose:
                        print(f"  [~] Normalized LF: {f.name}")
        print(f"  [+] Normalized line endings in {changed} text file(s)")

        # Step 6: Create zip archive
        print("\nStep 6: Creating zip archive...")
        zip_size = create_zip(pkg_dir, output_zip)
        print(f"  [+] Created {output_zip.name}")
        print(f"    Size: {zip_size / 1024:.1f} KB")

        # Step 7: Cleanup
        if not args.keep_temp:
            print("\nStep 7: Cleaning up temporary files...")
            shutil.rmtree(pkg_dir)
            print(f"  [+] Removed temporary package directory")
        else:
            print(f"\nStep 7: Keeping temporary directory: {pkg_dir}")

        # Summary
        print("\n" + "=" * 60)
        print("[SUCCESS] CTAN package created!")
        print("=" * 60)
        print(f"\nOutput file: {output_zip}")
        print(f"Package structure: {pkg_name}/ (flat layout)")
        print(f"Ready for CTAN submission at: https://ctan.org/upload")
        print("\nPackage contents:")
        print(f"  terminalcode/")
        print(f"    ├── README.md")
        print(f"    ├── LICENSE")
        print(f"    ├── CHANGELOG.md")
        print(f"    ├── {pkg_name}.sty")
        print(f"    └── {pkg_name}-doc.pdf")
        print()

        return 0

    except Exception as e:
        print(f"\n[ERROR] {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()

        # Cleanup on error
        if pkg_dir.exists():
            shutil.rmtree(pkg_dir)

        return 1


if __name__ == "__main__":
    sys.exit(main())
