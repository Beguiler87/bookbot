def count_words(text):
        words = text.split()
        return len(words)

def count_characters(text):
	char_counts = {}
	for char in text:
		char = char.lower()
		if char not in char_counts:
			char_counts[char] = 1
		else:
			char_counts[char] += 1
	return char_counts

def sort_on(char_counts):
	return char_counts["num"]

def chars_to_sorted_list(char_counts):
	chars_list = []
	for char, count in char_counts.items():
		chars_list.append({"char": char, "num": count})
	chars_list.sort(reverse=True, key=sort_on)
	return chars_list
