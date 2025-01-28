class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter สำหรับ name
    @property
    def name(self):
        return self._name

    # Setter สำหรับ name
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty!")
        self._name = value

    # Deleter สำหรับ name
    @name.deleter
    def name(self):
        print(f"Deleting name: {self._name}")
        del self._name  # ลบแอตทริบิวต์ _name

    # Getter สำหรับ age
    @property
    def age(self):
        return self._age

    # Setter สำหรับ age
    @age.setter
    def age(self, value):
        if value < 18 or value > 60:
            raise ValueError("Age must be between 18 and 60!")
        self._age = value

    # Deleter สำหรับ age
    @age.deleter
    def age(self):
        print(f"Deleting age: {self._age}")
        del self._age  # ลบแอตทริบิวต์ _age


# การใช้งาน
student = Student("John", 25)

# การเรียกใช้ Getter
print(student.name)  # Output: John
print(student.age)   # Output: 25

# การลบแอตทริบิวต์
del student.name  # Output: Deleting name: John
del student.age   # Output: Deleting age: 25

# การเข้าถึงหลังจากลบ
try:
    print(student.name)
except AttributeError as e:
    print(e)  # Output: 'Student' object has no attribute '_name'

try:
    print(student.age)
except AttributeError as e:
    print(e)  # Output: 'Student' object has no attribute '_age'
