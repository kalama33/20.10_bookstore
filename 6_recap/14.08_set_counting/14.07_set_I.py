"""_
Define a function named "unique_elements" that takes two parameters, "list1" and "list2" (both lists).
Convert "list1" and "list2" into sets named "set1" and "set2", respectively.
Create a new set named "unique_set" by taking the union of "set1" and "set2".
Convert "unique_set" back into a list named "unique_list" using the "list()" function.
Return "unique_list".summary_
"""

my_list1 = [1, 2, 3, 4, 5]
my_list2 = [4, 5, 6, 7, 8]

def unique_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    unique_set = set1.union(set2)
    
    unique_list = list(unique_set)
    
    return unique_list

print(unique_elements(my_list1,my_list2))

