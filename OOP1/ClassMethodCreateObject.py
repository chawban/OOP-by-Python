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
    def cerate_from_cls(cls, name, age):
        age = age+1
        return cls(name, age)  # สร้าง Object ของ Class
    
    @classmethod
    def change_class_attribute(cls, new_value):
        cls.species = new_value

    

# การสร้าง Object พร้อมกำหนดค่าเริ่มต้น
my_dog = Dog(name="Buddy", age=3)
my_dog2 = Dog(name="Pokki", age=5)
my_dog3 = Dog.cerate_from_cls(name="JhawToo", age=2)

#print(my_dog.species)
#print(my_dog2.species)
#my_dog.species ="DogDog"
#my_dog.change_class_attribute("DogDogCLS")
#print(Dog.species)
Dog.species = "DogDog chang by Class"
print(my_dog3.name)
print(my_dog3.age)


