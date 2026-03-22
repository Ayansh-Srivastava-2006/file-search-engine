🚀 File Search Engine

A high-performance local file search engine built with Python, featuring full-text indexing and fast retrieval using Whoosh and a Flask web interface.

✨ Features
🔍 Full-Text Search
Search through file contents (not just filenames) with fast indexing.
📄 Multiple File Support
Supports .txt and .pdf files (via PyPDF2).
🌐 Web Interface
Clean Flask-based UI with highlighted search results.
💻 CLI Interface
Search directly from your terminal.
⚡ Fast Indexing (Whoosh)
Efficient indexing for quick query responses.
🐳 Docker Support
Run the entire app in an isolated container.
📸 Demo

(Add screenshots here for maximum impact)

Example:

Query: "machine learning"

Result:

- file1.pdf → "...machine learning is a subset of AI..."
- notes.txt → "...introduction to machine learning concepts..."
🗂️ Project Structure
.
├── app.py        # Flask web app
├── indexer.py    # Builds search index
├── search.py     # Query logic
├── main.py       # CLI interface
├── utils.py      # PDF parsing & helpers
├── data/         # Your documents
└── indexdir/     # Search index storage
⚙️ Installation

1. Clone the Repository
git clone <https://github.com/Ayansh-Srivastava-2006/file-search-engine>
cd file-search-engine
2. Install Dependencies
pip install flask whoosh PyPDF2
▶️ Usage
Add Files

Place your .txt and .pdf files inside the data/ directory.

Run Web App
python app.py

Open:

<http://localhost:5000>
CLI Mode
python main.py
🔄 Reindex Files
Click Reindex in UI
OR
python indexer.py
🐳 Docker Setup
Build Image
docker build -t file-search-engine .
Run Container
docker run -p 5000:5000 \
-v ${PWD}/indexdir:/app/indexdir \
-v ${PWD}/data:/app/data \
file-search-engine
⚡ Performance
Uses Whoosh indexing for fast search retrieval
Handles large text datasets efficiently
Near real-time search after indexing
🚧 Future Improvements
🔎 Fuzzy search (typo tolerance)
📊 Relevance ranking improvements
📁 Support for more formats (.docx, .md)
🧠 Semantic search (AI-based)
🌍 Remote file indexing
🧠 Tech Stack
Python 3.10+
Flask
Whoosh
PyPDF2
Docker
🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

📜 License

    MIT License

💡 Author

    Ayash-Srivastava-2006
