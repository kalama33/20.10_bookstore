l1 = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10]
print(len(l1))

#Step 1

print(len(l1) // 2) #we get the middle index of l1
print(l1[len(l1) // 2]) # is this higher or lower than my item
l2 = l1[:len(l1)//2] # we dicarded half of our list
print(l2)

#Step 2

print(l2[len(l2)//2])
l3 = l2[:len(l2)//2]
print(l3)

#Step 3
print(l3[len(l3)//2])

#def binary_search(lst_sorted, value):
#   if lst_sorted[len(lst_sorted//2)] == value:
#       return True

lst_sorted = [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]

def binary_search(lst_sorted, value):
    if len(lst_sorted) == 0:
        return False

    mid = len(lst_sorted) // 2
    if lst_sorted[mid] == value:
        return True
    elif lst_sorted[mid] > value:
        return binary_search(lst_sorted[:mid], value)
    else:
        return binary_search(lst_sorted[mid+1:], value)
    
print(binary_search(lst_sorted, 101)) 