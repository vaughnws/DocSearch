#!/bin/bash
# Installation script for Document Search Tool (Mac/Linux)

echo "========================================"
echo "Doc Tool - Mac/Linux"
echo "========================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed!"
    echo "Please install Python 3 from https://www.python.org/downloads/"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed!"
    echo "Installing pip..."
    python3 -m ensurepip --upgrade
fi

echo "✓ pip3 found"
echo ""

# Upgrade pip first
echo "Upgrading pip..."
python3 -m pip install --upgrade pip
echo ""

# Install Python packages
echo "Installing required Python packages..."
echo ""

echo "[1/6] Installing Flask..."
pip3 install Flask==3.0.0 || pip3 install Flask

echo "[2/6] Installing PyPDF2..."
pip3 install PyPDF2==3.0.1 || pip3 install PyPDF2

echo "[3/6] Installing python-docx..."
pip3 install python-docx==1.1.0 || pip3 install python-docx

echo "[4/6] Installing python-pptx..."
pip3 install python-pptx==0.6.23 || pip3 install python-pptx

echo "[5/6] Installing Pillow..."
pip3 install "Pillow>=10.3.0" || pip3 install Pillow

echo "[6/6] Installing pytesseract..."
pip3 install pytesseract==0.3.10 || pip3 install pytesseract

echo ""
echo "✓ Python packages installed successfully!"
echo ""

# Check for Tesseract (optional for PNG OCR)
if command -v tesseract &> /dev/null; then
    echo "✓ Tesseract OCR found - PNG image search will work!"
else
    echo "   Tesseract OCR not found (optional)"
    echo "   PNG image text search will be limited."
    echo "   To install: brew install tesseract"
fi

echo ""
echo "========================================"
echo " Done, LFG NERDS!"
echo "========================================"
echo ""
echo "To start the search tool, run:"
echo "  ./run.sh"
echo "or"
echo "  python3 search_files.py"
echo ""
echo "Then open your browser to: http://127.0.0.1:5000"
echo ""
