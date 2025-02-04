class Dog:
    
    species = "Canine"  # Class attributes: ใช้ร่วมกันทุก instance
    
    # Constructor ที่มี Parameters
    # ใช้ self เพื่ออ้างถึง instance ปัจจุบัน
    def __init__(self, name, age):
        self.name = name  # Instance attributes: เฉพาะแต่ละ instance
        self.age = age    # Instance attributes: เฉพาะแต่ละ instance

    # ใช้ self เพื่ออ้างถึง instance ปัจจุบัน
    def bark(self): 
        print(f"{self.name} says Woof! Woof!")


    @classmethod
    def change_class_attribute(cls, new_value):
        cls.species = new_value

# การสร้าง Object พร้อมกำหนดค่าเริ่มต้น
my_dog = Dog(name="Buddy", age=3)
my_dog2 = Dog(name="Pokki", age=5)


print(my_dog.species)
print(my_dog2.species) 
my_dog.change_class_attribute("DogDogCLS") 
print(my_dog.species)
print(my_dog2.species)
 
Dog.change_class_attribute("เปลี่ยนผ่าน Dog")
#Dog.bark()
print(my_dog.species)
print(my_dog2.species)