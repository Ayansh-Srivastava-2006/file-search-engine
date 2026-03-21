from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
import os

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = create_in("indexdir", schema)
writer = ix.writer()

def index_files(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    writer.add_document(title=file, path=filepath, content=content)
            except:
                pass


index_files("data")

writer.commit()