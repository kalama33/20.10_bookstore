# task_3

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self): #  method is defined to handle the unary negation operation (-) on a Vector2d instance
        return Vector2d(-self.x, -self.y) # creates a new Vector2d object with the negated coordinates by negating self.x and self.y, and returns it.
                                          # applying the unary negation operator - to the vec2d instance, it creates a new Vector2d object neg_vec2d with the negated coordinates (-1, -1).
    def __str__(self):
        return f"Vector2d ({self.x}, {self.y})"

# original vec2d object remains unchanged, and the negation operation creates a new Vector2d object with the negated coordinates.
vec2d = Vector2d(1, 1)
neg_vec2d = -vec2d
print(vec2d)  # Output: Vector2d (1, 1)
print(neg_vec2d)  # Output: Vector2d (-1, -1)