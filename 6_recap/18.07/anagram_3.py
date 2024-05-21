from collections import Counter

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)

def group_anagram(lst):
    anagram_group = []   
    
    for index, word in enumerate(lst):
        print(index)
        for group in anagram_group:
            if is_anagram(word, group[0]):
                group.append(word)
                break
            print(group)
        else:
            anagram_group.append([word])
    return anagram_group        
    
print(group_anagram( ["dog", "god"]))

