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

    def cid(self,newname): 
        self.name = newname
        print(f"{self.name} says Woof! Woof!")

# การสร้าง Object พร้อมกำหนดค่าเริ่มต้น
my_dog = Dog(name="Buddy", age=3)
my_dog2 = Dog(name="Pokki", age=5)

# การเข้าถึง Attributes และ Methods
#print(f"My dog's name is {my_dog.name} and it's {my_dog.age} years old.")
# 
#Dog.species = "Mikki"  

#print(Dog.name)
my_dog2.species = "aaa"
print(my_dog.species)
print(my_dog2.species)

print(my_dog.name)
print(my_dog2.name)

"""
my_dog.species ="DogDog"
print(my_dog.species)
print(my_dog2.species)
print(Dog.species)
#print(Dog.name)  # error : ไม่มี Class attributes name

#Goto Dog2.py 

"""