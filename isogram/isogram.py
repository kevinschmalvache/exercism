def is_isogram(string):
    if string == "":
        return True
    string = string.replace('-', '').replace(' ', '').lower()
    letters_dict = {}
    for i in string:
        if letters_dict.get(i, 0) == 0:
            letters_dict[i] = 1
        else:
            letters_dict[i] += 1
    if sorted(letters_dict.values())[-1] == 1:
        return True
    return False