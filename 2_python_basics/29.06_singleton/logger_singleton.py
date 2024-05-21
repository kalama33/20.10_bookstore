"""La clase Singleton es responsable de garantizar que solo exista una instancia de la clase envuelta.
La variable de clase _instances es un diccionario que almacena las instancias de las clases.
En el método __init__, se inicializa la variable de instancia _class con la clase que se va a envolver.
El método __call__ se utiliza como un decorador para envolver la clase. Cuando se llama a la clase envuelta, este método se ejecuta.
Dentro de __call__, se verifica si la clase envuelta (self._class) no está en el diccionario _instances. Si no está presente, se crea una nueva instancia de la clase con self._class(*args, **kwargs) y se guarda en el diccionario _instances usando self._class como clave.
Finalmente, se devuelve la instancia del diccionario _instances correspondiente a la clase envuelta."""


class Singleton:
    _instances = {}
    
    def __init__(self, class_):
        self._class = class_
        
    def __call__(self, *args, **kwargs):
        if self._class not in self._instances:
            self._instances[self._class] = self._class(*args, **kwargs)
        return self._instances[self._class]

"""La clase Logger se declara y se aplica el decorador @Singleton, 
lo que garantiza que solo exista una instancia de Logger.
La clase Logger tiene un constructor __init__ que inicializa la lista de registros (logs) vacía.
El método add_log recibe un mensaje como entrada y lo agrega a la lista de registros (logs).
El método get_logs devuelve la lista de registros (logs)."""
    
@Singleton

class Logger:
    def __init__(self):
        self.logs = [] # register list
        
    def add_log(self, message): # add
        self.logs.append(message) 

    def get_logs(self):
        return self.logs   

"""Creamos tres instancias de Logger utilizando logger1 = Logger(), logger2 = Logger(), logger3 = Logger().
A cada instancia del Logger, le agregamos un mensaje de registro utilizando el método add_log.
Dado que se trata de un Singleton, todas las instancias de Logger comparten la misma lista de registros (logs).
Al imprimir los registros utilizando logger1.get_logs(), logger2.get_logs(), o logger3.get_logs(), obtenemos 
la misma lista de mensajes de registro que contiene todos los mensajes agregados anteriormente."""
    
 # Testing the Singleton Logger
logger1 = Logger() # create a unique instance of the class
logger1.add_log("Log message 1")

logger2 = Logger()
logger2.add_log("Log message 2")

logger3 = Logger()
logger3.add_log("Log message 3")

# All instances of the logger will have the same logs
print(logger1.get_logs())  # Output: ['Log message 1', 'Log message 2', 'Log message 3']
print(logger2.get_logs())  # Output: ['Log message 1', 'Log message 2', 'Log message 3']
print(logger3.get_logs())  # Output: ['Log message 1', 'Log message 2', 'Log message 3']        
      
    