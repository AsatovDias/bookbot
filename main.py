from stats import  *
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    total_words = get_nums_of_text_book(book)
    char_count_dict = get_numes_of_chars(book)
     
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(total_words)
    print("--------- Character Count -------")
    sorted_dict(char_count_dict)
    print("============= END ===============")

main()