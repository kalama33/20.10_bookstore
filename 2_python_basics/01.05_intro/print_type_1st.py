# Task 1 - printing single object


print(123)

print(43.23)

print(4-1j)

print("How are you?")

print(isinstance(123,int))


# Task 2 - printing type of given value


print(123, "is type of", type(123))

print(43.23, "is type of", type(43.23))

print(4-1j, "is type of", type(4-1j))

print("How are you?", "is type of", type("How are you?"))

print(isinstance(123, int), "is type of", type(isinstance(123,int)))


# Task 3 - checking type of value


# integer - True
number= 123
print(isinstance(number, int))

# float - False
number = 43.23
print(isinstance(number, int))

# complex - True
number = 4 - 1j
print(isinstance(number,complex))

# string - True
string = "Hello World!"
print(isinstance(str, str))

# boolean - False
boolean = "True"
print(isinstance(boolean, bool))


# Task 4 - checking type of value (version 2)


# integer -True
number = 123
print('Is', number, 'an instance of int?:', isinstance(number, int))  

# float - False
number = 43.23
print('Is', number, 'an instance of bool?:', isinstance(number, int))  

# complex - True
number = 4 - 1j
print("Is", number, "an instance of complex?:", isinstance(number, complex))

# boolean - False
boolean = True
print("Is", boolean, "an instance of bool?:", isinstance(boolean, bool))

# string - True
string = 123
print("Is", string, "an instance of str?:", isinstance(string, str))



# Task 5 - using comments in code


# These are my first comments (block comment)

print(123, "is type of", type(123))  # Getting type of object, str (inline comment)


'''
Multiline comment. Remember, the first word should be capitalized.  Use one or two spaces after a sentence-ending period.
Block comments generally apply to some (or all) code that follows them, and are intended to the same level as that code.
Inline comments is a comment on the same line as statement.  
'''


    