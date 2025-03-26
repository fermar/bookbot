def get_book_text(path):
    with open(path) as libro:
        cont = libro.read()
    # print(len(cont))
    return cont


def main():
    cont = get_book_text("books/frankenstein.txt")
    # print(len(cont))
    print(cont)


main()
