class Animal:
    def speak(self):
        print("สัตว์กำลังส่งเสียง")

class Dog(Animal):

    def speak(self):
        print("หมาเห่าโห้งๆ")

    def speak2(self):      
        # เรียกเมธอด speak ของคลาสแม่ (Animal)
        super().speak()
        
        

# สร้าง object จากคลาส Dog
my_dog = Dog()
my_dog.speak2()