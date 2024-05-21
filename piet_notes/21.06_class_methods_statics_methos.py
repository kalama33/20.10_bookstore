class MyClass:
    class_var = 0

    def __init__(self, instance_var):
        self.instance_var = instance_var

    def instance_method(self):
        self.instance_var += 1
        print(f" Instance method called")

    @classmethod
    def class_method(cls):
        cls.class_var += 1
        print(cls)
        print(f"class method called")

    @staticmethod
    def static_method():
        print('staic method called')

my_obj = MyClass(42)
my_obj.instance_method()
MyClass.class_method()