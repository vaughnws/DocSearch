
### For Mac/Linux:

1. **Run the installation script:**
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

2. **Start the search tool:**
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

3. **Open your browser to:**
   ```
   http://127.0.0.1:5000
   ```

### For Windows:

1. **Double-click:** `install.bat`

2. **Double-click:** `run.bat`

3. **Open your browser to:**
   ```
   http://127.0.0.1:5000
   ```

## Manual Installation

If the automated scripts don't work, you can install manually:

### Requirements:
- Python 3.7 or higher
- pip (Python package manager)

### Install dependencies:
```bash
# Mac/Linux:
pip3 install -r requirements.txt

# Windows:
pip install -r requirements.txt
```

### Run the application:
```bash
# Mac/Linux:
python3 search_files.py

# Windows:
python search_files.py
```

## How to Use

1. **Start the application** using one of the methods above
2. **Open your browser** to http://127.0.0.1:5000
3. **Type your search keywords** in the search box
4. **Press Enter** or click "Search"
5. **View results** with highlighted matches
6. **Click "Open File"** to open any document

## Optional: Enable Image Text Search -- This isnt working super well, so do it at your own risk.

To search text within PNG images, install Tesseract OCR:

**Mac:**
```bash
brew install tesseract
```

**Windows:**
Download from: https://github.com/UB-Mannheim/tesseract/wiki

## Troubleshooting

### "Python not found"
- Install Python from https://www.python.org/downloads/
- On Windows, make sure to check "Add Python to PATH" during installation

### "pip not found"
```bash
python3 -m ensurepip --upgrade  # Mac/Linux
python -m ensurepip --upgrade   # Windows
```

### "Module not found" errors
Run the install script again or manually install:
```bash
pip3 install -r requirements.txt  # Mac/Linux
pip install -r requirements.txt   # Windows
```

### Server won't start, or starts but exits immediately on mac/linux
- dont run with run.sh 
- open terminal and cd to this directory
- run this command:
```bash
python3 search_files.py
```

## File Structure

```
WEBSEC_MIDTERM/
├── search_files.py       # Main application
├── install.sh            # Mac/Linux installer
├── install.bat           # Windows installer
├── run.sh                # Mac/Linux launcher
├── run.bat               # Windows launcher
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Web interface
└── [your documents]      # All your files to search
```