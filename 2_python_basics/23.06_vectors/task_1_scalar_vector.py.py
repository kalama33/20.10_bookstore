# Task 1Scalar multiplicaiton

class Vector2d: # 2 dim vector
    def __init__(self, x, y): # atributes of the instance
        self.x = x
        self.y = y

    def __mul__(self, scalar): #  method is defined to handle the multiplication of a Vector2d instance with a scalar value. It creates a new Vector2d object with the coordinates multiplied by the scalar and returns it.
        return Vector2d(self.x * scalar, self.y * scalar)

    def __str__(self):  # string representation
        return f"Vector2d ({self.x}, {self.y})"

vec2d = Vector2d(1, 1)
new_vec2d = vec2d * 10
print(vec2d)  # Output: Vector2d (1, 1)En la función main(), se crea una instancia de la clase MathOperations llamada math_ops y se demuestra el comportamiento polimórfico llamando a cada método con diferentes números de argumentos.