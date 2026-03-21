from whoosh.index import open_dir
from whoosh.qparser import QueryParser

ix = open_dir("indexdir")

def search(query_str):
    results_list = []

    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query)

        for r in results:
            results_list.append((r['title'], r['path']))

    return results_list