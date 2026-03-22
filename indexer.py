print("RUNNING INDEXER")
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
import os

print("RUNNING:", __file__)
from utils import read_pdf

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

print("STEP 1")

ix = create_in("indexdir", schema)

print("STEP 2")

writer = ix.writer()

print("STEP 3")

def index_files(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            print("FILE FOUND:", file)
            filepath = os.path.join(root, file)

            try:
                if file.endswith(".txt"):
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                elif file.endswith(".pdf"):
                    content = read_pdf(filepath)

                else:
                    continue

                writer.add_document(title=file, path=filepath, content=content)

            except:
                pass


BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")

index_files(DATA_DIR)

writer.commit()