class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} Create object.")

    def __del__(self):
        print(f"{self.name} object is being deleted.")


obj = MyClass("Python") # Output: Python Create object..
del obj  # Output: Python object is being deleted.
#print(obj.name)