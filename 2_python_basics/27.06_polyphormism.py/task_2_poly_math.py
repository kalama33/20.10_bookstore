class MathOperations:
    
    # Cada método utiliza el operador *args para aceptar un número variable de argumentos.
    
    def add(self, *args): # El método add() utiliza la función sum() para sumar todos los argumentos y devuelve el resultado.
        return sum(args)

    def subtract(self, *args): # El método subtract() toma el primer argumento y luego resta los argumentos restantes en orden. Devuelve el resultado de la resta.
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    def multiply(self, *args): # El método multiply() multiplica todos los argumentos entre sí utilizando un bucle y devuelve el resultado de la multiplicación.
        result = 1
        for num in args:
            result *= num
        return result


def main(): # En la función main(), se crea una instancia de la clase MathOperations llamada math_ops y se demuestra el comportamiento polimórfico llamando a cada método con diferentes números de argumentos.
    math_ops = MathOperations()

    # Addition
    result = math_ops.add(2, 3)
    print(f"Addition Result: {result}")

    result = math_ops.add(4, 6, 8)
    print(f"Addition Result: {result}")

    # Subtraction
    result = math_ops.subtract(10, 3)
    print(f"Subtraction Result: {result}")

    result = math_ops.subtract(20, 5, 3)
    print(f"Subtraction Result: {result}")

    # Multiplication
    result = math_ops.multiply(2, 5)
    print(f"Multiplication Result: {result}")

    result = math_ops.multiply(3, 4, 2)
    print(f"Multiplication Result: {result}")


main()