from datetime import date

class Person:
    def __init__(self, fname, lname, birth_year):
        self.fname = fname
        self.lname = lname
        self.birth_year = birth_year

    @property
    def full_name(self):  # ใช้ @property เพื่อให้เรียกใช้งานเหมือน attribute
        return f"{self.fname} {self.lname}"

    @property
    def age(self):  # คำนวณอายุอัตโนมัติจากปีเกิด
        current_year = date.today().year
        return current_year - self.birth_year


if __name__ == '__main__':
    p = Person("Fah", "Puinon", 1998)

    print(p.full_name)  # ใช้งาน @property โดยไม่ต้องมี ()
    print(f"อายุ: {p.age} ปี")  # ใช้งาน @property เพื่อคำนวณอายุอัตโนมัติ

    # ลองแก้ไข full_name (จะเกิด AttributeError)
    try:
        p.full_name = "Songkarn Fahsai"
    except AttributeError as e:
        print("Error:", e)
