from datetime import date

#Python ทุกอย่างเป็น dynamic (runtime) 

class Person:
    def __init__(self, fname, lname, birth_year):
        self.fname = fname
        self.lname = lname
<<<<<<< HEAD
        self.birth_year = birth_year 
        self.__full_name = self.fname+" "+ self.lname
    
    @property    
    def full_name(self):   
        return f"ชื่อ : {self.fname} นามสกุล : {self.lname}"        
        
'''     
=======
        self.birth_year = birth_year
        self.full_name = fname+" "+lname


#    def full_name(self):   
#        return f"ชื่อ : {self.fname} นามสกุล : {self.lname}"


p = Person("ทักษิณ", "รักเรียน", 1998)

print(p.full_name)   

'''
p.full_name ="สมัคร พ่อครัว"   # ไม่ควรระบุแบบนี้โดยตรง
print(p.full_name)   

print(p.fname)
print(p.lname)   

print(p.full_name()) 

'''

#    print(f"อายุ: {p.age} ปี")  # ใช้งาน @property เพื่อคำนวณอายุอัตโนมัติ
    
#    p.full_name = "ประยุตย์ รักเล่น"

'''
>>>>>>> d985458d0721adff89b07f5312a95c53ac062ed3
    @property
    def full_name(self):  # ใช้ @property เพื่อให้เรียกใช้งานเหมือน attribute
        return f"{self.fname} {self.lname}"

    @property
    def age(self):  # คำนวณอายุอัตโนมัติจากปีเกิด
        current_year = date.today().year
        return current_year - self.birth_year
<<<<<<< HEAD
'''     
    

p = Person("ทักษิณ", "รักเรียน", 1998)

print(p.fname)
print(p.lname) 
print(p.birth_year) 
print(p.full_name) 
#p.full_name = "สมศรี มาค่ะ"
print(p.full_name) 

#print(p.age) 

    
#    def full_name(self):   
#        return f"ชื่อ : {self.fname} นามสกุล : {self.lname}"

'''
p = Person("ทักษิณ", "รักเรียน", 1998)

print(p.full_name)   


p.full_name ="สมัคร พ่อครัว"   # ไม่ควรระบุแบบนี้โดยตรง
print(p.full_name)   

print(p.fname)
print(p.lname)   

print(p.full_name) 

'''

#    print(f"อายุ: {p.age} ปี")  # ใช้งาน @property เพื่อคำนวณอายุอัตโนมัติ
    
#    p.full_name = "ประยุตย์ รักเล่น"




=======
'''
>>>>>>> d985458d0721adff89b07f5312a95c53ac062ed3
