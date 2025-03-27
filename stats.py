def get_book_text(path):
    with open(path) as libro:
        cont = libro.read()
    # print(len(cont))
    return cont


def word_count(cont):
    return len(cont.split())


def char_count(cont):
    countDics = []
    for char in cont:
        char = char.lower()
        if char.isalpha() == False:
            continue
        found = False
        for i, dic in enumerate(countDics):
            if dic["char"] == char:
                countDics[i]["count"] += 1
                found = True
                break
        if found == False:
            countDics.append({"char": char, "count": 1})

    return countDics
