def analyze_data(data):
    result = {
        "num_lists": 0,
        "num_dicts": 0,
        "num_tuples": 0,
        "total_list_elements": 0
    }
    
    for item in data:
        if isinstance(item, list):
            result["num_lists"] += 1
            result["total_list_elements"] += len(item)
        elif isinstance(item, dict):
            result["num_dicts"] += 1
        elif isinstance(item, tuple):
            result["num_tuples"] += 1
            
    return result

data = [
    {"name": "Alice", "age": 20},
    ("Bob", 22),
    [1, 2, 3],
    {"country": "USA", "city": "New York"},
    [4, 5, 6]
]

result = analyze_data(data)
print(result) 