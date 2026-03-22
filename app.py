import os
from whoosh.index import exists_in
from indexer import index_files

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
if not exists_in("indexdir"):
    print("Creating index inside Docker...")
    os.makedirs("indexdir", exist_ok=True)

    print("Files in data:", os.listdir(DATA_DIR))
    index_files(DATA_DIR)

from flask import Flask, render_template, request
from search import search
import subprocess

app = Flask(__name__)

@app.route("/reindex", methods=["POST"])
def reindex():
    subprocess.run(["python", "indexer.py"])
    return "Reindexing complete! Go back and search again."

@app.route("/", methods=["GET", "POST"])
def home():
    results = []

    if request.method == "POST":
        query = request.form.get("query", "")
        filetype = request.form.get("type", "all")

        results = search(query, filetype)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)