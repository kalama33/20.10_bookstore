from collections import deque

def is_palindrome(string):
    char_deque = deque(string)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

# Test cases
print(is_palindrome("radar"))  # True
print(is_palindrome("level"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("world"))  # False
