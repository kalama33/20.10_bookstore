def encode_to_bytes(input_str):
    encoded_bytes = input_str.encode("utf-8")
    return encoded_bytes

input_str = "Hello, 世界"
print(encode_to_bytes(input_str))
