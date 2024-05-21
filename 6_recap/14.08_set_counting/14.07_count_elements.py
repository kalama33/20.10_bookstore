"""
Define a function named "count_elements" that takes a single parameter, "lst" (a list).
Create an empty dictionary named "element_counts" to store the element frequencies.
Iterate over each element, "elem", in the list.
Inside the loop, try to use the "setdefault()" method on "element_counts" to update the frequency of "elem".
Return the "element_counts" dictionary.
"""


my_list = [1, 2, 3, 2, 1, 3, 1, 2, 3, 4, 5]

def count_elements(lst): # func
    element_counts = {} # empty dict
    for element in lst: # iterate
        element_counts.setdefault(element, 0) # method to update the frequency of the element in the dictionary
        element_counts[element] += 1          # checks if the key elem exists in the dictionary and, if not, adds it with a default value of 0
    return element_counts                     # increase the value associated with key elem by 1

result = count_elements(my_list)
print(result) 

print("_____________")


my_dict = {}
print(my_dict.setdefault("key", "bla"))
print(my_dict["key"])

"""
 Define a function named "group_by_length" that takes a single parameter, "strings" (a list of strings).
Create an empty dictionary named "grouped_strings" to store the grouped strings.
Iterate over each string, "string", in the list.
Inside the loop, use the "setdefault()" method on "grouped_strings" to set the default value for the length of "string" as an empty list.
Append "string" to the list associated with its length using the "append()" method.
Return the "grouped_strings" dictionary.   
"""

my_strings = ['apple', 'banana', 'car', 'dog', 'elephant', 'fruit', 'giraffe']
result = group_by_length(my_strings)
print(result)

def group_by_length(lst_of_strings):
    grouped_strings = {}
    for string in lst_of_strings:
        length_string = len(string)
        grouped_strings.setdefault(length_string, []).append(string)
    return grouped_strings
my_strings = ['apple', 'banana', 'car', 'dog', 'elephant', 'fruit', 'giraffe']
result = group_by_length(my_strings)
print(result)