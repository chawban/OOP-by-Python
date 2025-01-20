class Dog:
    # Constructor ที่มี Parameters
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof! Woof!")

# การสร้าง Object พร้อมกำหนดค่าเริ่มต้น
my_dog = Dog(name="Buddy", age=3)

# การเข้าถึง Attributes และ Methods
print(f"My dog's name is {my_dog.name} and it's {my_dog.age} years old.")
my_dog.bark()
