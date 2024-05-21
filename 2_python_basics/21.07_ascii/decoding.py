def decode_to_str(input_bytes):
    decode_str = input_bytes.decode("utf-8")
    return decode_str

input_bytes = b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
print(decode_to_str(input_bytes))