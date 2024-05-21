class Car:
    def drive(self):
        pass

class Sedan(Car):
    def drive(self):
        return "Driving a sedan"

class SUV(Car):
    def drive(self):
        return "Driving an SUV"

class CarFactory:
    def create_car(self, car_type):
        if car_type == "sedan":
            return Sedan()
        elif car_type == "suv":
            return SUV()
        else:
            raise ValueError("Invalid car type")
        
        
class Bike:
    def create

factory = CarFactory()
car1 = factory.create_car("sedan")
car2 = factory.create_car("suv")

print(car1 == car2)