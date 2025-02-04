class BankAccount:
    def __init__(self, name, balance):
        """ คอนสตรักเตอร์ (Constructor) ใช้สร้างบัญชีใหม่ """
        self.name = name  # Public Attribute
        self.__balance = balance  # Private Attribute

    def deposit(self, amount):
        """ เมธอดสำหรับฝากเงินเข้าบัญชี """
        if amount > 0:
            self.__balance += amount
            print(f"ฝากเงินสำเร็จ! ยอดเงินปัจจุบัน: {self.__balance} บาท")
        else:
            print("จำนวนเงินที่ฝากต้องมากกว่า 0 บาท")

    def withdraw(self, amount):
        """ เมธอดสำหรับถอนเงินจากบัญชี """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"ถอนเงินสำเร็จ! ยอดเงินคงเหลือ: {self.__balance} บาท")
        else:
            print("ยอดเงินไม่เพียงพอ หรือ จำนวนเงินที่ถอนต้องมากกว่า 0 บาท")

    def get_balance(self):
        """ เมธอดสำหรับตรวจสอบยอดเงินคงเหลือ """
        return self.__balance

    def show(self):
        """ แสดงชื่อบัญชี """
        print(f"ชื่อบัญชี: {self.name}")

    def showbalance(self):
        """ แสดงยอดเงินคงเหลือ """
        print(f"ยอดเงินคงเหลือ: {self.get_balance()} บาท")
        
    def transfer(self, amount, target_account):
        """ เมธอดสำหรับโอนเงินจากบัญชีนี้ไปยังบัญชีอื่น """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            target_account.deposit(amount)
            print(f"โอนเงิน {amount} บาท จากบัญชี {self.name} ไปยังบัญชี {target_account.name} สำเร็จ!")
        else:
            print("ยอดเงินไม่เพียงพอสำหรับการโอนเงิน")

# ------------------ ตัวอย่างการใช้งาน ------------------ #

# สร้างบัญชีใหม่
account1 = BankAccount("Somsee RukGung", 1000)
account2 = BankAccount("SomKhuan Narak", 5000)

account1.show()  # แสดงชื่อบัญชี
account1.showbalance()  # แสดงยอดเงินคงเหลือ

# โอนเงิน
account1.transfer(300, account2)  # โอนเงิน 300 บาทจาก account1 ไปยัง account2

# ตรวจสอบยอดเงินหลังโอน
account1.showbalance()  # ยอดเงินคงเหลือของ account1
account2.showbalance()  # ยอดเงินคงเหลือของ account2
