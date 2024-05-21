def merge_sort(arr, key='age'):
    # Base case: If the array has 1 or fewer elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the left and right halves
    left = merge_sort(left, key=key)
    right = merge_sort(right, key=key)

    # Merge the sorted halves
    return merge(left, right, key=key)


def merge(left, right, key='age'):
    merged = []  # List to store the merged result
    i = j = 0  # Pointers for the left and right halves

    # Compare elements from left and right halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements from the left half
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Add any remaining elements from the right half
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


dictionaries = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "David", "age": 28, "city": "Houston"},
    {"name": "Emma", "age": 27, "city": "San Francisco"},
    {"name": "Frank", "age": 32, "city": "Seattle"},
    {"name": "Grace", "age": 29, "city": "Boston"},
    {"name": "Henry", "age": 31, "city": "Dallas"},
    {"name": "Ivy", "age": 26, "city": "Miami"},
    {"name": "Jack", "age": 33, "city": "Denver"}
]

# Sort the dictionaries by age using the merge_sort function with the key='age'
sorted_dictionaries = merge_sort(dictionaries, key='age')

# Print the sorted list of dictionaries
print(sorted_dictionaries)
