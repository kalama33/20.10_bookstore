"""
Write a function that takes in a string of text and returns a dictionary containing 
the frequency of each word. You should use the `collections.Counter` class 
to implement the counting logic.
"""
from collections import Counter

text = "Hello world hello python hello world"

def count_word_frequencies(text):
    
    frequency_counter = Counter(text.split()) # split method
    
    return frequency_counter

text = "Hello world hello python hello world"
result = count_word_frequencies(text)
print(result)

### collections