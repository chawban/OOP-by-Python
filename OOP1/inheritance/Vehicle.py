class Vehicle:
    def __init__(self, started=False, speed=0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("สตาร์ทแล้ว ไปกันเลย!")

    def stop(self):
        self.speed = 0

    def increase_speed(self, delta):
        if self.started:
            self.speed += delta
            print("บรื้นนนน!")
        else:
            print("คุณต้องสตาร์ทเครื่องก่อน")

print ("-----------Vehicle-----------")
# สร้าง object จากคลาส Vehicle
my_car = Vehicle()

# เรียกใช้เมธอด start เพื่อสตาร์ทเครื่อง
my_car.start()

# เพิ่มความเร็ว
my_car.increase_speed(30)

# หยุดรถ
my_car.stop()

print(f"{my_car.speed}")   