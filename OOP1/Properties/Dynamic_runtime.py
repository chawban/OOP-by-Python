'''
Python ทุกอย่างเป็น dynamic (runtime) 
ซึ่งหมายความว่าสามารถเพิ่มหรือเปลี่ยนแปลง attributes ของ object ได้ตลอดเวลา
'''

class Person:
    def __init__(self, name):
        self.name = name  # สร้าง attribute name

# สร้าง object จาก class
p1 = Person("Alice")

# เพิ่ม attribute ใหม่ใน runtime
p1.age = 25
p1.city = "Bangkok"

# แสดงข้อมูล object
print(f"Name: {p1.name}")
print(f"Age: {p1.age}")
print(f"City: {p1.city}")
