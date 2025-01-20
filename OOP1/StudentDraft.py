# สร้าง Object นักศึกษา
student1 = Student("65001", "Alice", 2003)

# เพิ่มรายวิชา
student1.add_course("Mathematics")
student1.add_course("Physics")
student1.add_course("Mathematics")  

# แสดงรายวิชาที่ลงทะเบียน
student1.show_courses()
# Output:
# Registered Courses:
# 1. Mathematics
# 2. Physics

# ลบรายวิชา
student1.drop_course("Physics")
student1.show_courses()
# Output:
# Registered Courses:
# 1. Mathematics

student1.drop_course("Chemistry")  # แสดง Course not found
