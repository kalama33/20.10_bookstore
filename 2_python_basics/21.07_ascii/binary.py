def int_to_binary(input_int):
    binary_str = bin(input_int)[2:] #remove Ob prefix
    return binary_str

input_int= 42
print(int_to_binary(input_int))