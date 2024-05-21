list1 = [1, 2, 2, 3, 4, 5, 6]
list2 = [2, 4, 6, 8, 10]

def common_elements(list1, list2):
    common_list = []
    for number in list1:
        if number in list2: 
            common_list.append(number)
    return common_list


result = common_elements(list1, list2)
print("Common elements:", result)


def common_elements(list1, list2):
    return [(num, index) for index, num in enumerate(list1) if num in list2 and num not in list1[:index]]

result = common_elements(list1, list2)
print("Common elements:", result)


"""
def common_elements(list1, list2):
    
    common_list = ([num for num in list1 and list2 if num == num])
    
    return common_list
"""
    
    
    