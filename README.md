# Doc Search 
A fun loophole in certain instructions for an open-book midterm. 

## Loophole - Why this isnt against the exam policy

```code
The midterm will be open-book, allowing you to use the provided PowerPoint slides, PDFs and Word documents available on Learn.
However, internet access (including Google, AI tools, or other online resources) will not be permitted.
Additionally, merged files (PDF, Word, PowerPoint, etc.) are not allowed during the exam.
The midterm will last for 100 minutes and will consist of a combination of written responses, true/false, and multiple-choice questions.
```
- Only the PDFs from the Course Shell are allowed
- NO Internet access (No google, AI, or any Online Resources)
- NO Merged Files (Combined PDFs, Combined Slides, Combined Word files)

### How we stay within the policy
- Doc Search is locally hosted on port 5000, its offline, and doesnt have any internet access.
- Doc Search doesnt modify ANY files, they are exactly as downloaded from the course shell, no combinations or changes.
- Doc Search ONLY uses material from the course shell, no external resources, no AI, nothing else, just the provided slides and files :)

## How to run it
- cd into the WEBSEC_MIDTERM dir
### For Mac/Linux:
1. **Run the installation script:**
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

2a. **Start the search tool:**
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

2b. **Mac/Linux sometimes appends "exit" to the end of shell scripts
     - Run the python script directly if the run.sh closes immediately.
```bash
    python3 search_files.py
    # or:
    python3 search_files.py
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

## How it works:

- **Flask** - Web framework for handling HTTP requests
- **PyPDF2** - Extract text from PDF files
- **python-docx** - Read Word documents
- **Pillow** - Process images
- **pytesseract** - OCR (Optical Character Recognition) for extracting text from images - (This is optional, and isnt working reliably)
- **JavaScript** - Frontend logic
- **HTML+CSS** - Frontend structure


## Step-by-step logic

When you type a keyword and press "Search":
```javascript
async function performSearch() {
    const query = searchInput.value.trim();
    
    // Send POST request to /search endpoint
    const response = await fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query })
    });
    
    const data = await response.json();
    displayResults(data);
}
```
```python
@app.route('/search', methods=['POST'])
def search():
    """Handle search request"""
    query = request.json.get('query', '').strip()
    
    # Search through all files
    results = search_all_files(query)
    
    # Return results as JSON
    return jsonify({
        'query': query,
        'results': results,
        'total_files': len(results),
        'total_matches': sum(r['match_count'] for r in results)
    })
```
Then it searches the directory the server is running in:
```python
def search_all_files(query):
    results = []
    
    # Find all supported files
    supported_extensions = {'.pdf', '.docx'}
    files = [f for f in SEARCH_DIR.iterdir() 
             if f.is_file() and f.suffix.lower() in supported_extensions]
    
    # Search each file
    for file_path in files:
        ext = file_path.suffix.lower()
        matches = []
        
        if ext == '.pdf':
            matches = search_pdf(file_path, query)
        elif ext == '.docx':
            matches = search_docx(file_path, query)
        
        if matches:
            results.append({
                'filename': file_path.name,
                'filepath': str(file_path),
                'type': ext[1:].upper(),
                'matches': matches,
                'match_count': len(matches)
            })
    
    return results
```
Finally it appends the results to the HTML:
```javascript
function displayResults(data) {
    resultsDiv.innerHTML = '';
    
    // Loop through each result
    data.results.forEach(file => {
        const card = document.createElement('div');
        card.className = 'result-card';
        
        card.innerHTML = `
            <div class="result-header">
                <div class="result-filename">${file.filename}</div>
                <span class="match-count">${file.match_count} matches</span>
                <button class="open-file-btn">Open File</button>
            </div>
        `;
        
        resultsDiv.appendChild(card);
    });
}
```
