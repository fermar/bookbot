import sys

from stats import char_count, get_book_text, word_count


def sort_on(dict):
    return dict["count"]


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    libro = sys.argv[1]
    # libro = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {libro}...")
    cont = get_book_text(libro)
    print("----------- Word Count ----------")
    count = word_count(cont)
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    countCharDics = char_count(cont)
    countCharDics.sort(reverse=True, key=sort_on)
    for charDics in countCharDics:
        # cant = charDics["count"]
        print(f"{charDics["char"]}: {charDics["count"]}")
    # print(cont)
    print("============= END ===============")


main()
