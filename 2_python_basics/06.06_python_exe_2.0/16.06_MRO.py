class A:
    def __init__(self):
        print("Initializing class A")
        super().__init__()

class B(A):
    def __init__(self):
        print("Initializing class B")
        super().__init__()

class C(A):
    def __init__(self):
        print("Initializing class C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("Initializing class D")
        super().__init__()
        
"""The order of the output is based on the Method Resolution Order (MRO) and the activation sequences. In this case, class D inherits from class B and class C, which in turn both inherit from class A.

When an instance of class D is created, its constructor __init__() is called. Within the constructor of class D, the line super().__init__() is executed, which triggers the constructors of its superclasses in the order specified by the MRO.

The MRO is determined using the C3 linearization algorithm, which follows a depth-first left-to-right approach. In this case, the MRO for class D is [D, B, C, A], indicating the order in which the superclasses are traversed.

Based on the MRO, the constructors are called in the following sequence:

Initializing class D: The constructor of class D is called first.
Initializing class B: Since class B is the next superclass according to the MRO, its constructor is called.
Initializing class C: Next, the constructor of class C is called.
Initializing class A: Finally, the constructor of class A is called.
This sequence ensures that each class's constructor is called exactly once, following the MRO and the inheritance hierarchy.""""