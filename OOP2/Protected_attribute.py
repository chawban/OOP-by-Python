class MyClass:
    def __init__(self):
        self._protected_var = 20  # แอตทริบิวต์ protected

    def get_protected(self):
        return self._protected_var

# สร้างอ็อบเจ็กต์
obj = MyClass()



# การเข้าถึงแอตทริบิวต์ที่เป็น protected โดยตรง
print(obj._protected_var)  # Output: 20
