class WeirdNUmber:
    def __init__(self,value):
        self.value = value
    
    def __repr__(self):
        return f"{self.value}"
    
    def __add__(self, other):
        return WeirdNumber(self.value - other.value)
    
    def __sub__(self,other):
        return WeirdNumber(self.value + other.value)
    
wn1 = WeirdNUmber(15)
wn2 = WeirdNUmber(2)

print(wn1 - wn2)
print(wn1 + wn2)