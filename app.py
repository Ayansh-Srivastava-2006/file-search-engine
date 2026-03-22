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
    app.run(debug=True)