from search import search

while True:
    q = input("Search: ")
    results = search(q)

    for title, path in results:
        print(f"{title} → {path}")