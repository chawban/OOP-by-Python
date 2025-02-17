from Vehicle import Vehicle  # Importing the Vehicle class from Vehicle.py       
    #Vehicle ตัวแรก (หลัง from) หมายถึงชื่อไฟล์หรือโมดูล (Vehicle.py)
    #Vehicle ตัวที่สอง (หลัง import) หมายถึงคลาส Vehicle ที่อยู่ในไฟล์นั้น


# คลาสแม่ Vehicle (Parent Class)
# คลาสลูก (Child Class) Car สืบทอดคุณสมบัติจาก Vehicle
class Car(Vehicle):
    def __init__(self, started=False, speed=0, trunk_open=False):
        # เรียก constructor ของคลาสแม่ (Vehicle)
        super().__init__(started, speed)
        # กำหนดค่าเริ่มต้นสำหรับแอตทริบิวต์ของ Car
        self.trunk_open = trunk_open

    def open_trunk(self):
        self.trunk_open = True
        print("เปิดกระโปรงหลังรถแล้ว")

    def close_trunk(self):
        self.trunk_open = False
        print("ปิดกระโปรงหลังรถแล้ว")
  
print ("-----------Car-----------")        
# สร้าง object จากคลาส Car
my_car = Car(started=False, speed=0, trunk_open=False)

# เรียกใช้เมธอด start จากคลาสแม่ (Vehicle)
my_car.start()

# เพิ่มความเร็ว
my_car.increase_speed(30)

# เปิดกระโปรงหลังรถ
my_car.open_trunk()

# ปิดกระโปรงหลังรถ
my_car.close_trunk()          