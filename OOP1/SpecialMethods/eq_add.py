class MyClass:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __add__(self, other):
        return self.value + other.value

obj1 = MyClass(5)
obj2 = MyClass(5)
obj3 = MyClass(10)
print(obj1 == obj2)  # Output: True
print(obj2 == obj3)  # Output: False

print("===========") 
print(obj2 + obj3)  # Output: 15
