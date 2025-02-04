class EmployeeOLD:
    def __init__(self, name, age):
        self._name = name  # Attribute ที่กำหนดค่าใน constructor
        self._age = age    # Attribute ที่กำหนดค่าใน constructor
        self._bonus = None  # Attribute ที่ไม่มีค่าเริ่มต้นใน constructor

    # Method สำหรับดึงค่า '_name'
    def getName(self):
        print("Getting name")
        return self._name

    # Method สำหรับกำหนดค่า '_name'
    def setName(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        print("Setting name")
        self._name = value

    # Method สำหรับดึงค่า '_age'
    def getAge(self):
        print("Getting age")
        return self._age

    # Method สำหรับกำหนดค่า '_age'
    def setAge(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a positive integer")
        print("Setting age")
        self._age = value

    # Method สำหรับดึงค่า '_bonus' (Attribute ที่ไม่มีค่าเริ่มต้น)
    def getBonus(self):
        if self._bonus is None:
            print("No bonus assigned yet")
        else:
            print("Getting bonus")
        return self._bonus

    # Method สำหรับกำหนดค่า '_bonus'
    def setBonus(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Bonus must be a positive number")
        print("Setting bonus")
        self._bonus = value

    # Method สำหรับลบค่า '_bonus'
    def deleteBonus(self):
        print("Deleting bonus")
        self._bonus = None


# การใช้งาน
emp = Employee("Alice", 30)

# เรียกใช้ method getName() และ getAge()
print(emp.getName())  # Output: Getting name \n Alice
print(emp.getAge())   # Output: Getting age \n 30

# เรียกใช้ method getBonus() (ยังไม่มีค่า)
print(emp.getBonus())  # Output: No bonus assigned yet \n None

# กำหนดค่าใหม่ให้ attribute โดยใช้ method setName(), setAge(), และ setBonus()
emp.setName("Bob")    # Output: Setting name
emp.setAge(25)        # Output: Setting age
emp.setBonus(5000)    # Output: Setting bonus

# ดึงค่าใหม่จาก method getName(), getAge(), และ getBonus()
print(emp.getName())  # Output: Getting name \n Bob
print(emp.getAge())   # Output: Getting age \n 25
print(emp.getBonus())  # Output: Getting bonus \n 5000

# ลบค่า '_bonus' โดยใช้ method deleteBonus()
emp.deleteBonus()     # Output: Deleting bonus
print(emp.getBonus())  # Output: No bonus assigned yet \n None