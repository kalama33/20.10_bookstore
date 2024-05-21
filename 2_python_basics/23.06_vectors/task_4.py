# Task 4

"""method is defined to handle the addition operation (+) between 
two Vector2d instances. It first checks if the vectors have the same length. 
If not, it raises a ValueError. Then, it performs element-wise addition of 
the values in the vectors using a list comprehension and returns a new 
Vector2d object with the resulting values."""

class Vector2d:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must have the same length")
        
        """Luego, realiza la suma de los valores de los vectores 
        elemento por elemento usando una comprensión de lista y 
        devuelve un nuevo objeto Vector2d con los valores resultantes"""
        
        result = [x + y for x, y in zip(self.values, other.values)] 
        return Vector2d(result)

    def __str__(self):
        return f"Vector2d({self.values})"

v1 = Vector2d([3, 4, 5, 5, 8])
v2 = Vector2d([6, 7, 8, 8, 9])
v3 = v1 + v2
print(v3)  # Output: Vector2d([9, 11, 13])