def find_anagrams(word, candidates):
    anagrams = []
    for item in candidates:
        if sorted(word.lower()) == sorted(item.lower()) and word.lower() != item.lower():
                anagrams.append(item)
    return anagrams
