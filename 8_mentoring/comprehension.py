# by writing the elements

list1 = ["first", "second", "third"]
print(list1)

# by multiplication

list2 = [0] * 10
print(list2)

# by a classical for loop

list3 = list()
for i in range (10):
    list3. append(i)
    
print(list3)

# List Comprehension
# shorter syntex

list4 = [0,1,2,3,4,5,6,7,8]
newlist4 = [x for x in list4 if x % 2 ==0]

print(newlist4)

list5 = [x for x in range(10)]
print(list5)

# List with list elementes

list_1 = [1,2,3]

list_2 = ["a","b","c"]

list_3 = [True, False, True]

big_list = [list_1, list_2, list_3]

print(big_list)

print(big_list[0][2])

# append a to big list

big_list[0].append(4)
print(big_list[0])

list_5 = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]

print(list_5)

# Trying with list multiplication

# Simple case no nested list

list = [0] * 10

print(list)

list[1]=1

#print(lisst)

print("________________")

inner_list = [0,0,0,0]

outer_list = [[0]*4]*3

print(outer_list)

outer_list[0][1]=1

proper_outer_list = [[0 for x in range(4)] for y in range(3)]

print(proper_outer_list)


# The proper way to define nested list by list comprehension 

proper_outer_list[1].append(5)

proper_outer_list[1] = proper_outer_list[1] + [6,7,8]

print(proper_outer_list)

proper_outer_list.append(["a","b","c"])

print(proper_outer_list)

ls = [1,2,3]

vowels = ["a", "e", "i", "o", "u"]
vowelsCSV = ",".join(vowels)
print()

# decorators (take func as an arg)

def func_sum_low(num1,num2):
    return num1 + num2

def func_prod_low(num1,num2):
    return num1 * num2

def func_do_something():
    return 5

def func_op(selector, function_list):
    
    if selector ==1:
        return function_list[0]
    else:
        return function_list[1]
    
myfunc = func_op(1[func_sum_low, func_prod_low])
print(myfunc(1,3))

myfunc = func_op(0[func_sum_low, func_prod_low])
print(myfunc(1,3))

# initial tax calculation
#19%

def total_price_with_tax(initial_price):
    
    return initial_price * 1.19

#test it
print(total_price_with_tax(1000))

# let's write a decorator
# adding 5% additional
# we do not want to change the implementation
# we pass the func. as an argument

def decorator(func):
    
# define the new func. based on the input func. 
# so I get another functionality based on the existing one
    
    def inner(arg):
        return func(arg) * 1.05
    return inner

total_price_with_tax = decorator

new_tax_function = decorator(total_price_with_tax)

total_final_price = new_tax_function(1000)

print(total_final_price)