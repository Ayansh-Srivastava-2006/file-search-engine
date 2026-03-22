from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
import os
from utils import read_pdf

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True)    )

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = create_in("indexdir", schema)

writer = ix.writer()

def index_files(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            
            filepath = os.path.join(root, file)
            print("Indexing:", filepath)
            try:
                if file.endswith(".txt"):
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                elif file.endswith(".pdf"):
                    content = read_pdf(filepath)

                else:
                    continue

                writer.add_document(title=file, path=filepath, content=content)
                print("Added to index:", file)

            except:
                pass


BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
index_files(DATA_DIR)

writer.commit()