class Dog:
    species = "Canine"  # Class Attribute

    def __init__(self, name):
        self.name = name  # Instance Attribute

dog1 = Dog("เจ้าตูบ")
dog2 = Dog("เจ้าดำ")

print(Dog.species)  # Output: Canine
print(dog1.species)  # Output: Canine
print(dog2.species)  # Output: Canine

#Dog.species = "สัตว์เลี้ยงลูกด้วยนม"

#print(Dog.species)  # Output: สัตว์เลี้ยงลูกด้วยนม
#print(dog1.species)  # Output: สัตว์เลี้ยงลูกด้วยนม
#print(dog2.species)  # Output: สัตว์เลี้ยงลูกด้วยนม
