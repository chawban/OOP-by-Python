class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"MyClass instance with name: {self.name}"

obj = MyClass("Python")
print(obj)  # Output: MyClass instance with name: Python
