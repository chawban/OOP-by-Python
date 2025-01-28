class Student:
    def __init__(self, name, age):
        self._name = name  # ใช้ _ เพื่อบ่งชี้ว่าเป็น private attribute
        self.age = age     # Use setter to validate age during initialization

    # Getter สำหรับ name
    @property
    def name(self):
        return self._name

    # Setter สำหรับ name
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty!") # จะพูดถึงอีกครั้งใน Exception
        self._name = value

    # Getter สำหรับ age
    @property
    def age(self):
        return self._age

    # Setter สำหรับ age
    @age.setter
    def age(self, value):
        if value < 18 or value > 60:
            raise ValueError("Age must be between 18 and 60!")  # The age must be in range
        self._age = value

        
# จะพูดถึงอีกครั้งใน Exception
try:
    student = Student("Somchai", 61)  # จะเกิด ValueError
except ValueError as e:
    print(e)  # Output: Age must be between 18 and 60!

# การเรียกใช้ Getter
print(student.name)  # Output: Somchai (if age was valid)
print(student.age)   # Output: 20 (if age was valid)

# การเรียกใช้ Setter
student.name = "Sheemoy"
student.age = 22

print(student.name)  # Output: Sheemoy
print(student.age)   # Output: 22