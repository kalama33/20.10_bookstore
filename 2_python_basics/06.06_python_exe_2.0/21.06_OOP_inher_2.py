class Person:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Employee(Person): # corrige, anade super class
    def __init__(self):
        super().__init__()
        self.__salary = 0

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def print_name(self):
        print(self.get_name())


# Crear una instancia de la clase Employee
employee = Employee()

# Establecer el nombre, edad y salario utilizando los métodos apropiados
employee.set_name("John Doe")
employee.set_age(30)
employee.set_salary(5000)

# Obtener el nombre, edad y salario utilizando los métodos apropiados
print("Employee Name:", employee.get_name())       # ---> John Doe
print("Employee Age:", employee.get_age())         # ---> 30
print("Employee Salary:", employee.get_salary())   # ---> 5000
employee.print_name()                               # ---> John Doe
