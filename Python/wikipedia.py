import wikipedia

search_word = input("Wikipedia> ")

print(f"search results:\n{wikipedia.search(search_word)}\n")
print(f"search summary:{wikipedia.summary(search_word, sentences=1)}")
