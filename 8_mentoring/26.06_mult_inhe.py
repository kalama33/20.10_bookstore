
class A:
    def __init__(self):
        print("init of A called")
class B(A):
    def __init__(self):
        print("init of B called")
b = B()
9:19
# When we override __init__ method we have to explicitly call the __init__ to super class if needed

class C(A):
    def __init__(self):
        print("init of C called")
        super().__init__()
c = C()

# A case with arguments

class A:
    def __init__(self,val1):
        self.value1 = val1
        print(f"init of A called and value is {self.value1}")
class C(A):
    def __init__(self, val1, val2):
        self.value2 = val2
        print(f"init of C called and second value is {self.value2}")
        super().__init__(val1)
c = C(1,2)

