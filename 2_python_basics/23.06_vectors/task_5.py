# Task 5 

"""modificado el método __add__ para manejar dos casos diferentes. 
Si el objeto pasado como parámetro es una instancia de Vector2d, 
realiza la suma de los valores de los vectores como lo hicimos anteriormente. 
Si el objeto pasado es una lista, realiza la suma elemento por elemento entre 
la lista y los valores del vector."""

"""Es importante destacar que el método __add__ maneja el caso en el que 
se pasa un objeto que no es ni una instancia de Vector2d ni una lista, 
generando un TypeError en ese caso. Esto evita sumar el objeto Vector2d 
con tipos de datos no compatibles."""

class Vector2d:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        if isinstance(other, Vector2d):
            if len(self.values) != len(other.values):
                raise ValueError("Vectors must have the same length")
            result = [x + y for x, y in zip(self.values, other.values)]
            return Vector2d(result)
        elif isinstance(other, list):
            if len(self.values) != len(other):
                raise ValueError("The list must have the same length as the vector")
            result = [x + y for x, y in zip(self.values, other)]
            return Vector2d(result)
        else:
            raise TypeError("Cannot add a Vector2d object with this type of data")

    def __str__(self):
        return f"Vector2d({self.values})"

list_v1 = [3, 4, 5]
v2 = Vector2d([6, 7, 8])
v3 = list_v1 + v2
print(v3)  # Output: Vector2d([9, 11, 13])
