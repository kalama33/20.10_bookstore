# define and add attributes
class Car:
    def __init__(self, make, model, year, color): #not running method as param.
        self.make = make
        self.model = model 
        self.year = year 
        self.color = color
        self.is_running = False
        
# define methods
    def start(self):
        self.is_running = True
        
    def stop(self):
        self.is_running = False
        
    def get_status(self):
        if self.is_running:
            return "Car is running"
        return "Car is not running"
    
    # to print and describe add __str__    
    def __str__(self):
        #print("trigger") 
        return f"Car: {self.make} {self.model} ({self.year}), Color: {self.color}, Status: {self.get_status()}"

# instance       
car_1 = Car(make = "Jaguar", model= "XX", year = "1987", color ="black")
print(car_1)

#str(car_1)
#car_1.__str__()
#print(car_1.get_status())
#car_1.start()
#print(car_1.get_status())
