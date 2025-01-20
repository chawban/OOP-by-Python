class MyClass:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

obj1 = MyClass(5)
obj2 = MyClass(5)
print(obj1 == obj2)  # Output: True

