# 1st task

print(1987)
print(70.40)
print(15-3j)
print("Hi, I am  a Machine, and i will destroy you")
print(isinstance("Hello", str))

#2nd task

print(1987 ,"is type of", (type (1987)))
print(70.40 ,"is type of", (type(70.40)))
print(15-3j ,"is type of", (type(15-3j)))
print("Hi, I am a Machine" ,"is type of", (type("Hi, I am a Machine")))
print(True,"is a type of", (type(True)))

#3rd task

print(isinstance(1987, int))
print(isinstance(70.40, str))
print(isinstance(15-3j, complex))
print(isinstance("Hi", str))
print(isinstance(1987, str))

#4th task

values = [1987, 70.40, 15-3j, True, 'Hi']
types = [int, bool, complex, bool, float]

for value, type_ in zip(values, types):
    print(f"Is {value} an instance of {type_.__name__}?: {isinstance(value, type_)}")

