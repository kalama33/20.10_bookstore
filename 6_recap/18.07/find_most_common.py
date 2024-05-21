from collections import Counter

elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

def find_most_common_elements(elements, n):
    
    element_counter = Counter(elements)
    
    most_common = element_counter.most_common(n)
    
    return most_common

def find_most_common_elements(elements, n):
    
    element_counter = Counter(elements)
    print(element_counter.keys()) # dic keys = tuple
    print(element_counter.items()) # dic items = list of tuples
    
    #list of tuples with k and v           
    max_value = max(element_counter.values())
    sorted_values = sorted(element_counter.values(), reverse = True)
    print(sorted_values[:n])
    n_most_common = sorted_values[:n]
    
    result = []
    
    for key, value in element_counter.items():
        if value in n_most_common:
            result.append((value, key))
        
    return result

# Test the function
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
result = find_most_common_elements(elements, 2)
print(result)

