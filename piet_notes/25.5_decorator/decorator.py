# Define the decorator named uppercase
def uppercase(func):
    # Define the wrapper function that wraps the original function
    def wrapper():
        # Call the original function to get the result
        result = func()
        # Convert the result to uppercase
        return result.upper()
    # Return the wrapper function
    return wrapper

# Decorate the get_message function with the uppercase decorator
@uppercase
def get_message():
    return "Welcome to Python!"

# Call the decorated function
message = get_message()
# Print the result
print(message)  # WELCOME TO PYTHON!