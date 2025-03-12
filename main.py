import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_characters_by_count

def get_book_text(book_path):
    book_text = ""
    with open(book_path) as book:
        book_text = book.read()
    return book_text

def check_args(run_args):
    if len(run_args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    check_args(sys.argv)
    book_filepath = sys.argv[1]
    book_text = get_book_text(book_filepath)
    book_word_count = get_word_count(book_text)
    book_character_count = get_character_count(book_text)
    sorted_character_count = sort_characters_by_count(book_character_count)
    
    bookbot_title = "============ BOOKBOT ============"
    word_title = "----------- Word Count ----------"
    character_title = "--------- Character Count -------"
    end_title = "============= END ==============="

    analyzing_message = f"Analyzing book found at {book_filepath}..."
    word_message = f"Found {book_word_count} total words"

    print(bookbot_title)
    print(analyzing_message)
    print(word_title)
    print(word_message)
    print(character_title)
    for character_count in sorted_character_count:
        if character_count["character"].isalpha():
            print(f"{character_count["character"]}: {character_count["count"]}")
    print(end_title)

main()