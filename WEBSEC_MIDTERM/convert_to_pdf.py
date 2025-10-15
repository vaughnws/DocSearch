#!/usr/bin/env python3
"""
Multi-format to PDF Converter
Supports: PPTX, DOCX, PNG, and skips existing PDFs
"""

import os
import platform
from pathlib import Path

# Required packages:
# pip install pillow

def convert_png_to_pdf(input_path, output_path):
    """Convert PNG images to PDF"""
    from PIL import Image
    
    try:
        image = Image.open(input_path)
        # Convert RGBA to RGB (PNG with transparency)
        if image.mode in ('RGBA', 'LA', 'P'):
            rgb_image = Image.new('RGB', image.size, (255, 255, 255))
            if image.mode == 'P':
                image = image.convert('RGBA')
            rgb_image.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
            image = rgb_image
        elif image.mode != 'RGB':
            image = image.convert('RGB')
        
        image.save(output_path, 'PDF', resolution=100.0)
        print(f"✓ Converted: {input_path.name} -> {output_path.name}")
        return True
    except Exception as e:
        print(f"✗ Error converting {input_path.name}: {str(e)}")
        return False

def convert_docx_to_pdf_mac(input_path, output_path):
    """Convert DOCX to PDF on macOS using Word"""
    import subprocess
    
    try:
        script = f'''
        tell application "Microsoft Word"
            activate
            open POSIX file "{input_path.absolute()}"
            set docPath to POSIX file "{output_path.absolute()}"
            save as active document file name (docPath as string) file format format PDF
            close active document saving no
        end tell
        '''
        result = subprocess.run(['osascript', '-e', script], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(f"✓ Converted: {input_path.name} -> {output_path.name}")
            return True
        else:
            print(f"✗ Error converting {input_path.name}: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Error converting {input_path.name}: {str(e)}")
        return False

def convert_pptx_to_pdf_mac(input_path, output_path):
    """Convert PPTX to PDF on macOS using PowerPoint"""
    import subprocess
    
    try:
        script = f'''
        tell application "Microsoft PowerPoint"
            activate
            open POSIX file "{input_path.absolute()}"
            save active presentation in POSIX file "{output_path.absolute()}" as save as PDF
            close active presentation saving no
        end tell
        '''
        result = subprocess.run(['osascript', '-e', script], 
                              capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print(f"✓ Converted: {input_path.name} -> {output_path.name}")
            return True
        else:
            print(f"✗ Error converting {input_path.name}: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Error converting {input_path.name}: {str(e)}")
        return False

def convert_to_pdf(input_path, output_path=None):
    """Main conversion function"""
    input_path = Path(input_path)
    
    if not input_path.exists():
        print(f"✗ File not found: {input_path}")
        return False
    
    # Generate output path if not provided
    if output_path is None:
        output_path = input_path.with_suffix('.pdf')
    else:
        output_path = Path(output_path)
    
    # Skip if already PDF
    if input_path.suffix.lower() == '.pdf':
        print(f"⊘ Skipped (already PDF): {input_path.name}")
        return True
    
    # Skip if output already exists
    if output_path.exists():
        print(f"⊘ Skipped (output exists): {output_path.name}")
        return True
    
    # Get file extension
    ext = input_path.suffix.lower()
    system = platform.system()
    
    # Route to appropriate converter
    if ext == '.png':
        return convert_png_to_pdf(input_path, output_path)
    
    elif ext == '.docx':
        if system == 'Darwin':
            return convert_docx_to_pdf_mac(input_path, output_path)
        else:
            print(f"✗ DOCX conversion not supported on {system}")
            return False
    
    elif ext == '.pptx':
        if system == 'Darwin':
            return convert_pptx_to_pdf_mac(input_path, output_path)
        else:
            print(f"✗ PPTX conversion not supported on {system}")
            return False
    
    else:
        print(f"✗ Unsupported file type: {ext}")
        return False

def batch_convert(directory, recursive=False):
    """Convert all supported files in a directory"""
    directory = Path(directory)
    
    if not directory.is_dir():
        print(f"✗ Not a directory: {directory}")
        return
    
    print(f"\n{'='*60}")
    print(f"Converting files in: {directory}")
    print(f"Recursive: {recursive}")
    print(f"{'='*60}\n")
    
    # Supported extensions
    supported = {'.pdf', '.pptx', '.docx', '.png'}
    
    pattern = '**/*' if recursive else '*'
    files = [f for f in directory.glob(pattern) 
             if f.is_file() and f.suffix.lower() in supported]
    
    if not files:
        print("No supported files found.")
        return
    
    print(f"Found {len(files)} file(s) to process\n")
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for file_path in files:
        result = convert_to_pdf(file_path)
        if result:
            if file_path.suffix.lower() == '.pdf':
                skip_count += 1
            else:
                success_count += 1
        else:
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"Conversion Complete!")
    print(f"  Converted: {success_count}")
    print(f"  Skipped:   {skip_count}")
    print(f"  Errors:    {error_count}")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file:  python3 convert_to_pdf.py input_file.pptx [output.pdf]")
        print("  Batch mode:   python3 convert_to_pdf.py --batch directory/")
        print("  Recursive:    python3 convert_to_pdf.py --batch directory/ --recursive")
        print("\nSupported formats: PPTX, DOCX, PNG (PDFs are skipped)")
        sys.exit(1)
    
    if sys.argv[1] == '--batch':
        if len(sys.argv) < 3:
            print("Please specify a directory for batch conversion")
            sys.exit(1)
        batch_convert(sys.argv[2], recursive='--recursive' in sys.argv)
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_to_pdf(input_file, output_file)
