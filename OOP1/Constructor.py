class Dog:
    
    species = "Canine"  # Class Attribute
    
    # Constructor ที่มี Parameters
    def __init__(self, name, age, sound="Woof"):
        self.name = name  # Instance variable
        self.age = age    # Instance variable
        self.sound = sound    # Instance variable     

    def bark(self):
        print(f"{self.name} ร้อง {self.sound}")

# การสร้าง Object พร้อมกำหนดค่าเริ่มต้น
my_dog = Dog(name="Buddy", age=3)

# การเข้าถึง Attributes และ Methods
print(f"My dog's name is {my_dog.name} and it's {my_dog.age} years old.")
my_dog.bark()
