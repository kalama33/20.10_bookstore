
class Car:
    def__init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False
        
    def start(self):
        self.is_running = True
        
    def stop(self):
        self.is_running = False