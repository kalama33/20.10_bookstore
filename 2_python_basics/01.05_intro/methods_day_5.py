### String methods ###

my_text = "this is a TEST"

changed = my_text.upper()
print(my_text.upper())      #Method = .
print(my_text.capitalize())
print(my_text.lower())
print(my_text.isalpha()) # alpha = part of the alphabet (if there is a space is not)
print(my_text.isalnum()) # allnum = alphanumeric

print(my_text.split()) #Splits the string, spaces into a list
print(my_text.split("a")) # Same but it takes a letter out
    # we got a list                        


# isupper()
# endwith(...)
# strip() remove the spaces
# count('l')
# find("ll")

long_text = """
It was a dark and stormy night
Ya ya, ding dong
The end.
"""

print(long_text.split("\n"))

print("A nice kitten".replace("kitten", "dragon"))

desc = "A mage conjured an image of a dragon"
print(desc.replace("mage", "wizard")) #oops

text = "Joel\"Req\" Peltonen" 
#What is the "\" character called again?
#It is the scape character in python.

print("--------------------")

# It is a function 
print(len("caramel ice")) # count the charachters
print(len(["water", "snow", "ice"])) # count the items 
 # int has no lenght

### list methods ###

drinks = ["Coffee", "Tea", "Water"]
print(drinks[0])

drinks.append("Juice")
drinks.append(7)
print(drinks)

drinks.insert(2, "cola") #insert in a specific position
print(drinks)

### Piet, more methods ###

";".join(["Hello", "world", "again"])
         
    # Joining strings with first element

# To generate csv files

"Hello world".casefold()

### Concatenation

"Hello" + "" + "Hello"
#- "Hello World"

"The sum of 1 + 2 is {0}".format(1+2)
#- "The sum of 1 + 2 is 3"

word1="hello"
word2="world"
f"{word1.capitalize()} {word2.capitalize()}" #formated string literal
f"{word1} {word2}"
word1 + "" + word2

print(f"{word1.capitalize()} {word2.capitalize()}")

# %

name = "John"
age = 30
print("My name is %s and %d years old." % (name,age))
print("%s" % "BLA") # ???

### Index and Slicing

# - Slice, extract a piece of your string 

#   string[start:end:step]

my_string = "Hello, World"

print(my_string[0:5])

print(my_string[1:6:1])

print(my_string[::2])

### String Immutability

# - They can not be modify in-place
