# Class to represent Address as an object
class Address:
    def __init__(self, street, city, zip_code):
        self.street = street    # string type
        self.city = city        # string type
        self.zip_code = zip_code  # string type

    def __str__(self):
        return f"ถนน {self.street}, เมือง {self.city}, รหัสไปรษณีย์ {self.zip_code}"

# Class to represent Student, with Address as an attribute (object datatype)
class Student:
    def __init__(self, name, age, address):
        self.name = name        # string type
        self.age = age          # integer type
        self.address = address  # Address object (object datatype)

    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}, Address: {self.address}"

# Creating an Address object
student_address = Address("123 Main St", "Udon Thani", "41000")

# Creating a Student object with the Address object as an attribute
student1 = Student("Somchai Udon", 20, student_address)

# Printing the student's details
print(student1)

print(student1.address.street)
print(student1.address.city)