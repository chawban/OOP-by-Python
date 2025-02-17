#Employee.py

class Employee:
    def __init__(self, name, age):
        self._name = name  # Attribute ที่กำหนดค่าใน constructor
        self._age = age    # Attribute ที่กำหนดค่าใน constructor
        self._bonus = None  # Attribute ที่ไม่มีค่าเริ่มต้นใน constructor

    # Getter สำหรับ '_name'
    @property
    def name(self):
        print("Getting name")
        return self._name

    # Setter สำหรับ '_name'
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        print("Setting name")
        self._name = value

    # Getter สำหรับ '_age'
    @property
    def age(self):
        print("Getting age")
<<<<<<< HEAD
        #self._age = self._age+10
=======
>>>>>>> d985458d0721adff89b07f5312a95c53ac062ed3
        return self._age

    # Setter สำหรับ '_age'
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a positive integer")
        print("Setting age")
        self._age = value
<<<<<<< HEAD
        
        
 
    # Getter สำหรับ '_bonus' (Attribute ที่ไม่มีค่าเริ่มต้น)print(emp.bonus)
=======
'''
    # Getter สำหรับ '_bonus' (Attribute ที่ไม่มีค่าเริ่มต้น)
>>>>>>> d985458d0721adff89b07f5312a95c53ac062ed3
    @property
    def bonus(self):
        if self._bonus is None:
            print("No bonus assigned yet")
        else:
            print("Getting bonus")
        return self._bonus

<<<<<<< HEAD
    # Setter สำหรับ '_bonus'   emp.bonus = 5000 
=======
    # Setter สำหรับ '_bonus'
>>>>>>> d985458d0721adff89b07f5312a95c53ac062ed3
    @bonus.setter
    def bonus(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Bonus must be a positive number")
        print("Setting bonus")
        self._bonus = value

    # Deleter สำหรับ '_bonus'
    @bonus.deleter
    def bonus(self):
        print("Deleting bonus")
        self._bonus = None
<<<<<<< HEAD

=======
'''
>>>>>>> d985458d0721adff89b07f5312a95c53ac062ed3

# การใช้งาน
emp = Employee("Alice", 30)

<<<<<<< HEAD
#emp.age = "one"
=======
>>>>>>> d985458d0721adff89b07f5312a95c53ac062ed3
# เรียก getter ของ 'name' และ 'age'
print(emp.name)  # Output: Getting name \n Alice
print(emp.age)   # Output: Getting age \n 30

<<<<<<< HEAD


=======
>>>>>>> d985458d0721adff89b07f5312a95c53ac062ed3
# เรียก getter ของ 'bonus' (ยังไม่มีค่า)
print(emp.bonus)  # Output: No bonus assigned yet \n None

# เรียก setter ของ 'bonus' เพื่อกำหนดค่าใหม่
emp.bonus = 5000  # Output: Setting bonus
print(emp.bonus)  # Output: Getting bonus \n 5000

<<<<<<< HEAD
''' 
# เรียก deleter ของ 'bonus' เพื่อลบค่า
del emp.bonus     # Output: Deleting bonus
print(emp.bonus)  # Output: No bonus assigned yet \n None

''' 
=======
# เรียก deleter ของ 'bonus' เพื่อลบค่า
del emp.bonus     # Output: Deleting bonus
print(emp.bonus)  # Output: No bonus assigned yet \n None
>>>>>>> d985458d0721adff89b07f5312a95c53ac062ed3
