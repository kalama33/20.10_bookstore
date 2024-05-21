# func and

# with and if first operand is false = false. If true, second eval.
def evaluate_expression(a, b):
    result = a and b
    if result == False and a == True:
        print("Short circuit evaluation occurred!")
    return result

# test
print(evaluate_expression(True, False))
print(evaluate_expression(False, True))
print(evaluate_expression(False, False))
print(evaluate_expression(True, True))

print("\n")

# func or
# with or if first operand is true = true. If first op. is false, then check the second
def evaluate_expression_or(a, b):
    result = a or b
    if result == True and a == False:
        print("Short circuit evaluation occurred!")
    return result

#test 
print(evaluate_expression_or(True, False))
print(evaluate_expression_or(False, True))
print(evaluate_expression_or(False, False))
    