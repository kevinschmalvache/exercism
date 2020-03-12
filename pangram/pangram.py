ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def is_pangram(sentence):
    occurrences = set()
    for character in sentence.lower():
        occurrences.add(character)
    for searchedCharacter in ALPHABET:
        if searchedCharacter not in occurrences:
            return False
        else:
            occurrences.remove(searchedCharacter)
    return True