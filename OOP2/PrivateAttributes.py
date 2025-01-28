class MyClass:
    def __init__(self):
        self.__private_var = 10  # จะถูกเปลี่ยนชื่อเป็น _MyClass__private_var

    def get_private(self):
        return self.__private_var

# สร้างอ็อบเจ็กต์
obj = MyClass()

# การเข้าถึงแอตทริบิวต์ที่เป็น private โดยตรงจะทำให้เกิด AttributeError
try:
    print(obj.__private_var)
except AttributeError as e:
    print(e)  # Output: 'MyClass' object has no attribute '__private_var'

# การเข้าถึงแอตทริบิวต์ที่ถูก mangled โดยใช้ชื่อภายใน
print(obj._MyClass__private_var)  # Output: 10
