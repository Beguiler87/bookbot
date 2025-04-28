import sys
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
path = sys.argv[1]

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
		return file_contents

from stats import count_words

from stats import count_characters

from stats import chars_to_sorted_list

def main():
	text = get_book_text(path)
	num_words = count_words(text)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	char_counts = count_characters(text)
	print("--------- Character Count -------")
	sorted_chars = chars_to_sorted_list(char_counts)
	for char_dict in sorted_chars:
		if char_dict["char"].isalpha():
			print(f"{char_dict['char']}: {char_dict['num']}")
	print("============= END ===============")

main()
