class Animal:
    def __init__(self, name):
        self.name = name
        print(f"สัตว์ชื่อ {self.name} ถูกสร้างแล้ว")

class Dog(Animal):
    def __init__(self, name, breed):
        # เรียก constructor ของคลาสแม่ (Animal)
        super().__init__(name)
        self.breed = breed
        print(f"สุนัขพันธุ์ {self.breed} ถูกสร้างแล้ว")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # เรียกใช้ constructor ของคลาสแม่
        self.color = color
    
    def make_sound(self):
        return "Meow! Meow!"

# สร้าง object จากคลาส Dog
my_dog = Dog("บัดดี้", "ลาบราดอร์")


cat = Cat("Kitty", "White")
print(cat.name)        # ใช้คุณสมบัติจากคลาสแม่
print(cat.color)       # คุณสมบัติใหม่ที่เพิ่มในคลาสลูก
print(cat.make_sound())
#print(cat.breed)
