"""
Write a function that takes in a list of words and groups the anagrams together. 
An anagram is a word formed by rearranging the letters of another word. 
You should use the `collections.Counter` class to implement the grouping logic.
"""
from collections import Counter

words = ['cat', 'dog', 'tac', 'god', 'act']

def group_anagrams(words):
    group_of_a = {}
    for word in words:
        print(sorted(word)) # sorting alphab.
        chars = sorted(word)
        #key = tuple(chars)
        key = "".join(chars)
        group_of_a.setdefault(key,[]).append(word) # {'act': ['cat', 'tac', 'act'], 'dgo': ['dog', 'god']}
    return list(group_of_a.values()) # [['cat', 'tac', 'act'], ['dog', 'god']]





"""
def group_anagrams(words):
    
    anagram_dict = {}
    
    for word in words:
        letter_count = Counter(word) # count occurrences of letters in word
        key = tuple(sorted(letter_count.items())) # sorted tuple of items. key in the anagram dict.
        if key in anagram_dict:
            anagram_dict[key].append(word) # if key exist in dict is append
        else:
            anagram_dict[key] = [word] # if not, new entry created

    return list(anagram_dict.values())
"""
result = group_anagrams(words)
print(result)
    
        
        
    