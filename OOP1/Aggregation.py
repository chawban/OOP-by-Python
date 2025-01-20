class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []  # Weak association: students exist independently of teacher

    def add_student(self, student):
        self.students.append(student)

# สร้างออบเจกต์
student1 = Student("Somchai")
student2 = Student("Ananya")
teacher = Teacher("Ajarn Somsak")

teacher.add_student(student1)
teacher.add_student(student2)

del teacher  # นักเรียนยังคงอยู่ แม้อาจารย์จะถูกลบไปแล้ว




"""
ความหมาย: เป็นความสัมพันธ์แบบ "เชื่อมโยงกัน" (has-a relationship) ที่แสดงถึงการเชื่อมต่อแบบอิสระ
การเชื่อมโยง: ออบเจกต์ที่เป็นส่วนประกอบ (component) มีชีวิตของตัวเองและสามารถมีเจ้าของได้มากกว่าหนึ่ง
ความเป็นเจ้าของ:
ถ้าออบเจกต์เจ้าของถูกลบ ออบเจกต์ส่วนประกอบยังคงอยู่
ความสัมพันธ์มีความอ่อนแอกว่า (weak dependency)
"""