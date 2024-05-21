from collections import Counter

def is_anagram(word1,word2):
    
    chars_word1 = Counter(word1)
    chars_word2 = Counter(word2)
    if chars_word1 == chars_word2:
        return True
    #elif chars_word1 != chars_word2:
    return False
 
   
def is_anagram(word1,word2):
    return Counter(word1) == Counter(word2)
    
    #chars_word1 = Counter(word1)
    #chars_word2 = Counter(word2)    

result = is_anagram("cat","tac")
print(result)
    
result = is_anagram("kot","tac")
print(result)


    