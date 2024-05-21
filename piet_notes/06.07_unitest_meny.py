class Dollar:
    def __init__(self, number):
        self.amount = number
        
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

import unittest

class TestMoney(unittest.TastCase):
    def testMultiplication(self):
        five = Dollar(5)
        tenner = five.times(2)
        
        
"""
Este código representa una clase llamada "Dollar" que tiene dos métodos. 
El método __init__ se utiliza para inicializar la instancia de la clase con un número dado. 
El método times multiplica la cantidad (amount) de la instancia actual por un multiplicador dado y 
devuelve una nueva instancia de la clase "Dollar" con el resultado de la multiplicación.

Luego, se importa el módulo unittest, que es un framework de pruebas unitarias en Python. 
Se define una clase llamada "TestMoney" que hereda de unittest.TestCase, que es la clase base para 
definir pruebas en unittest. Dentro de esta clase, se define un método de prueba llamado testMultiplication.

En este método de prueba, se crea una instancia de la clase "Dollar" con un valor de 5. 
Luego, se llama al método times en esa instancia con un multiplicador de 2. 
Esto crea una nueva instancia de "Dollar" llamada "tenner" que contiene el resultado de la multiplicación (10).

Este código está destinado a realizar pruebas unitarias para asegurarse de que 
el método times funcione correctamente. En las pruebas unitarias, se verifican las expectativas y
se comparan los resultados esperados con los resultados reales para asegurarse de que el código se comporte como se espera.
"""