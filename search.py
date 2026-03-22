from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser

ix = open_dir("indexdir")

def search(query_str, filetype="all"):
    results_list = []

    with ix.searcher() as searcher:
        parser = MultifieldParser(["title", "content"], schema=ix.schema)
        query = parser.parse(query_str)
        results = searcher.search(query)

        for r in results:
            path = r['path']
            if filetype == "pdf" and not path.endswith(".pdf"):
                continue
            if filetype == "txt" and not path.endswith(".txt"):
                continue

            snippet = r.get('content', '')[:200].replace(
                query_str,
                f"<mark>{query_str}</mark>"
            )

            results_list.append((r['title'], path, snippet))

    return results_list