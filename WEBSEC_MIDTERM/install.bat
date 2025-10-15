@echo off
REM Installation script for Document Search Tool (Windows)

echo ========================================
echo Doc Tool - Windows
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed!
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo X pip is not installed!
    echo Installing pip...
    python -m ensurepip --upgrade
)

echo [OK] pip found
echo.

REM Upgrade pip first
echo Upgrading pip...
python -m pip install --upgrade pip
echo.

REM Install Python packages one by one with better error handling
echo Jorking It...
echo.

echo [1/6] Installing Flask...
pip install Flask==3.0.0
if errorlevel 1 (
    echo Warning: Flask installation had issues, trying without version...
    pip install Flask
)

echo [2/6] Installing PyPDF2...
pip install PyPDF2==3.0.1
if errorlevel 1 (
    echo Warning: PyPDF2 installation had issues, trying without version...
    pip install PyPDF2
)

echo [3/6] Installing python-docx...
pip install python-docx==1.1.0
if errorlevel 1 (
    echo Warning: python-docx installation had issues, trying without version...
    pip install python-docx
)

echo [4/6] Installing python-pptx...
pip install python-pptx==0.6.23
if errorlevel 1 (
    echo Warning: python-pptx installation had issues, trying without version...
    pip install python-pptx
)

echo [5/6] Installing Pillow...
pip install "Pillow>=10.3.0"
if errorlevel 1 (
    echo Warning: Pillow installation had issues, trying latest version...
    pip install Pillow
)

echo [6/6] Installing pytesseract...
pip install pytesseract==0.3.10
if errorlevel 1 (
    echo Warning: pytesseract installation had issues, trying without version...
    pip install pytesseract
)

echo.
echo [OK] Jorked!
echo.

REM Check for Tesseract (optional for PNG OCR)
tesseract --version >nul 2>&1
if errorlevel 1 (
    echo [!] Tesseract OCR not found (optional)
    echo     PNG image text search will be limited.
    echo     To install: Download from https://github.com/UB-Mannheim/tesseract/wiki
) else (
    echo [OK] Tesseract OCR found - PNG image search will work!
)

echo.
echo ========================================
echo Done, LFG NERDS!
echo ========================================
echo.
echo To start the search tool, run:
echo   run.bat
echo or
echo   python search_files.py
echo.
echo Then open your browser to: http://127.0.0.1:5000
echo.
pause
