from collections import Counter
def group_anagrams(lst):
    anagram_group = []  # List to store the groups of anagrams
    for word in lst:
        for group in anagram_group:
            # Check if the word has the same letter count as the first word in the group
            if Counter(word) == Counter(group[0]):
                group.append(word)  # Add the word to the anagram group
                break
        else:
            # If no existing group is found, create a new group with the word
            anagram_group.append([word])
    return anagram_group
words = ['cat', 'dog', 'tac', 'god', 'act']
result = group_anagrams(words)
print(result)

def group_anagrams(lst1):
    anagram_groups = [] # result
    word_count = [] # count of the first element
    for word in lst1:
        count = Counter(word)
        for index, value in enumerate(word_count):
            if count == value:
                anagram_groups[index].append(word)
                break
        else:
            anagram_groups.append([word])
            word_count.append(count)
    return anagram_groups
# Test the function
words = ['cat', 'dog', 'tac', 'god', 'act']
result = group_anagrams(words)
print(result)