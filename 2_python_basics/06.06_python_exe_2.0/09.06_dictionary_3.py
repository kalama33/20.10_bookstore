def merge_sort(arr, key_func=None):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left, key_func=key_func)
    right = merge_sort(right, key_func=key_func)

    return merge(left, right, key_func=key_func)


def merge(left, right, key_func=None):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key_func is None:
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        else:
            if key_func(left[i]) <= key_func(right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# Test cases
print(merge_sort([2, 5, 1, 3, 4]))  # Sorts the list elements directly

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

print(merge_sort(dictionaries, key=lambda item: item['city']))  # Sorts the dictionaries by 'city' key
print(merge_sort(dictionaries, key=lambda item: item['name']))  # Sorts the dictionaries by 'name' key
print(merge_sort(dictionaries, key=lambda item: item['age']))   # Sorts the dictionaries by 'age' key
