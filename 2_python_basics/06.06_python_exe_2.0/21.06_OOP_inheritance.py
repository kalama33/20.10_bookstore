# Create a parent class

class Person:
    def __init__(self,name,age):
        self.name = ""
        self.age = 0
    
    def set_name(self, name):
        self.name = name
        
    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
        
class Employee(Person):
    def __init__(self,name, age, salary):
        super().__init__(name,age)
        self.salary = 0
        
    def set_salary(self,salary):
        self.set_salary = salary
    
    def get_salary(self):
        return self.salary
    
    def print_name(self):
        print(self.get_name())
    
    
# Create an instance of the Employee class
employee = Employee("Joe", 30, 60000)



# Get the name, age, and salary using the appropriate methods
print("Employee Name:", employee.get_name()) #---> John Doe
print("Employee Age:", employee.get_age())  #---> 30
print("Employee Salary:", employee.get_salary())  #---> 5000
employee.print_name() #--> John Doe