class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance Attribute
        self.age = age    # Instance Attribute

dog1 = Dog("เจ้าตูบ", 3)
dog2 = Dog("เจ้าดำ", 5)

print(dog1.name)  # Output: เจ้าตูบ
print(dog2.name)  # Output: เจ้าดำ
