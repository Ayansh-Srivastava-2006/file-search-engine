from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser
from whoosh.qparser import QueryParser
from whoosh.highlight import HtmlFormatter



def search(query_str, filetype="all"):
    ix = open_dir("indexdir")
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

            results.formatter = HtmlFormatter(tagname="mark")
            results.fragmenter.charlimit = 200

            snippet = r.highlights("content")

            if not snippet:
                snippet = r.get("content", "")[:200]

            results_list.append((r['title'], path, snippet))

    return results_list