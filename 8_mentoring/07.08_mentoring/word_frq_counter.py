from collections import Counter
import re

def word_frequency_counter(file_path):
    # Read the text file and tokenize words
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\w+', text.lower())  # Tokenize words and convert to lowercase

    # Count the frequency of each word
    word_count = Counter(words)

    # Print words and frequencies in descending order
    for word, frequency in word_count.most_common():
        print(f"{word}: {frequency}")

# Provide the path to your text file
#file_path = "path/to/your/text/file.txt"
#word_frequency_counter(file_path)