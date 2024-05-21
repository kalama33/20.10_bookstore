def string_to_ascii(input_str):
    ascii_list = [ord(char) for char in input_str]
    return ascii_list

# Test the function
input_str = "Hello"
print(string_to_ascii(input_str))