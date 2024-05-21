# Task 2

"""The combination of __mul__ and __rmul__ allows the scalar multiplication operation to work in both orders: vector * scalar and scalar * vector."""

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, scalar): # defined to handle the multiplication of a Vector2d instance with a scalar value
        return Vector2d(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar): #  method is defined to handle the reverse order of the multiplication, where the scalar value is on the left side of the * operator. It simply calls the __mul__ method with the operands reversed, effectively achieving the desired behavior.
        return self.__mul__(scalar)

    def __str__(self):
        return f"Vector2d ({self.x}, {self.y})"

vec2d = Vector2d(1, 1)
new_vec2d = 10 * vec2d
print(vec2d)  # Output: Vector2d (1, 1)
print(new_vec2d)  # Output: Vector2d (10, 10)