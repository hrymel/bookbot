def get_num_words(book_text):
	# splits the book into word chunks and checks the length
	num_words = len(book_text.split())
	return num_words

def get_characters_in_book(book_text):
    # convert the whole text to lowercase to avoid duplicate entries
    lower_case_text = book_text.lower()
    alphabet_dict = {}

    # loop directly over each character in the lowercase text
    for char in lower_case_text:
        if char in alphabet_dict:
            alphabet_dict[char] += 1  # increment count if already exists
        else:
            alphabet_dict[char] = 1   # start count at 1 if first occurrence

    return alphabet_dict

def sort_on(dict):
    return dict["num"]


def return_sorted(char_dict):
    # Create a list of dictionaries with "char" and "num" keys
    chars_list = []
    for char, count in char_dict.items():
    	if char.isalpha():
        	chars_list.append({"char": char, "num": count})
    
    # Sort the list in descending order by the "num" value
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list