from stats import get_num_words, get_characters_in_book, return_sorted
import sys

def get_book_text(file_path):
	#takes file_path as arg and reads it as a var
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents

def main(file_path_to_book):
    book_text = get_book_text(file_path_to_book)
    num_words = get_num_words(book_text)
    char_dict = get_characters_in_book(book_text)
    chars_sorted_list = return_sorted(char_dict)  

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    main(sys.argv[1])

