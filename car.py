class Car(Vehicle):
    def __init__(self, started=False, speed=0, trunk_open=False):
        # เรียก constructor ของคลาสแม่ (Vehicle)
        super().__init__(started, speed)
        # กำหนดค่าเริ่มต้นสำหรับแอตทริบิวต์ของ Car
        self.trunk_open = trunk_open

    def open_trunk(self):
        if self.started:
            print("ไม่สามารถเปิดกระโปรงหลังรถได้ขณะที่เครื่องยนต์กำลังทำงาน")
        else:
            self.trunk_open = True
            print("เปิดกระโปรงหลังรถแล้ว")

    def close_trunk(self):
        self.trunk_open = False
        print("ปิดกระโปรงหลังรถแล้ว")