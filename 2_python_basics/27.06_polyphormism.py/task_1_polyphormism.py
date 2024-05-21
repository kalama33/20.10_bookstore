# Task 1

from functools import singledispatch

"""" 
se importa singledispatch de functools. Luego, el método neg se define como 
una función normal decorada con @singledispatch. A continuación, se definen las 
implementaciones específicas para cada tipo utilizando el decorador @neg.register(type) 
y una función anónima _ como el método correspondiente.
"""

class Negator:
    """
    singledispatch es un decorador utilizado para definir funciones genéricas y permite seleccionar 
    diferentes implementaciones basadas en el tipo del argumento.
    Aplica el decorador singledispatch al método neg de la clase Negator. 
    Esto indica que el método neg se comportará como una función genérica y permitirá diferentes 
    implementaciones según el tipo de argumento.
    """               
    @singledispatch                
    def neg(self, arg): # Define el método neg que toma dos parámetros: self (referencia al objeto Negator) y arg (el argumento que se va a negar)
        raise NotImplementedError("Cannot negate a")
    
    @neg.register(int) # Registra una implementación específica del método neg para el tipo int. La función anónima _(self, arg) se asociará con este tipo.
    def _(self, arg):
        return -arg

    @neg.register(bool)
    def _(self, arg):
        return not arg

    @neg.register(str)
    def _(self, arg):
        return ""
        

obj = Negator() # Crea una instancia de la clase Negator y la asigna a la variable obj.
print(obj.neg(-1)) 
print(obj.neg(True))
print(obj.neg("Hello"))