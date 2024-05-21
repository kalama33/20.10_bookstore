from collections import Counter

string = "hellow world"

def counter_unique_characters(str):
    char_counter = Counter(str)
    return char_counter
    
print(counter_unique_characters(string))
print(counter_unique_characters("abracadabra"))