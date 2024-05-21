"""_
Define a function named "common_elements" that takes two parameters, "list1" and "list2" (both lists).
Convert "list1" and "list2" into sets named "set1" and "set2", respectively.
Create a new set named "common_set" by taking the intersection of "set1" and "set2".
Convert "common_set" back into a list named "common_list" using the "list()" function.
Return "common_list".summary_
"""

my_list1 = [1, 2, 3, 4, 5]
my_list2 = [4, 5, 6, 7, 8]

def common_elements(list1, lis2):
    set1 = set(list1)
    set2 = set(list2)
    
    common_set = set1.intersection(set2)
    common_list = list(common_set)
    
    return common_list

    
    