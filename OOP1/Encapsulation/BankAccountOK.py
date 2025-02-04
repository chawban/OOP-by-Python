class BankAccount:
    def __init__(self, name, balance):
        """
        คอนสตรักเตอร์ (Constructor) ใช้สร้างบัญชีใหม่
        :param name: ชื่อเจ้าของบัญชี (เป็น public attribute)
        :param balance: ยอดเงินคงเหลือ (เป็น private attribute)
        """
        self.name = name  # Public Attribute (เข้าถึงได้จากภายนอก)
        self.__balance = balance  # Private Attribute (ซ่อนจากภายนอก)
       # print("----------- Create : "+self.name+" Balance :"+self.__balance+"------------------")       
        print("----------- Create : "+self.name+"------------------")       

    def deposit(self, amount):
        """ เมธอดสำหรับฝากเงินเข้าบัญชี """
        if amount > 0:
            self.__balance += amount
            print(f"ฝากเงินสำเร็จ! ยอดเงินปัจจุบัน: {self.__balance} บาท")
        else:
            print("จำนวนเงินที่ฝากต้องมากกว่า 0 บาท")
            return  False

    def withdraw(self, amount):
        """ เมธอดสำหรับถอนเงินจากบัญชี """
        if 0 < amount <= self.__balance:
            self.__balance -= amount   # a-=b   a=a-b
            print(f"ถอนเงินสำเร็จ! ยอดเงินคงเหลือ: {self.__balance} บาท")
            return  True
        else:
            print("ยอดเงินไม่เพียงพอ หรือ จำนวนเงินที่ถอนต้องมากกว่า 0 บาท")
            return  False

    def get_balance(self):
        """ เมธอดสำหรับตรวจสอบยอดเงินคงเหลือ """
        return self.__balance  # คืนค่าจำนวนเงินที่ซ่อนอยู่

    # ✅ แก้ไขเมธอด show() และ showbalance() ให้ถูกต้อง
    def show(self):
        """ แสดงชื่อบัญชี """
        print(f"ชื่อบัญชี: {self.name}")

    def showbalance(self):
        """ แสดงยอดเงินคงเหลือ โดยใช้ get_balance() """
        print(f"ยอดเงินคงเหลือ: {self.get_balance()} บาท")

    def show_other_account(self,target_account): 
        print(f"ชื่อบัญชีเราคือ: {self.name} ชื่อบัญชีคุณคือ {target_account.name}")
        
        
    def tranfer(self,  target_account): #amount,
        print("===========โอนเงิน=================")
        self.withdraw(1000)
        target_account.deposit(1000)
        
        
# ------------------ ตัวอย่างการใช้งาน ------------------ #

# สร้างบัญชีใหม่
account1 = BankAccount("Somsee RukGung", 1000)
account1.show()  # ✅ แสดงชื่อบัญชี
account1.showbalance()  # ✅ แสดงยอดเงินคงเหลือ


# ฝากและถอนเงิน
account1.deposit(500)
account1.withdraw(300)



# สร้างบัญชีใหม่ให้กับ SomKhuan Narak
account2 = BankAccount("SomKhuan Narak", 55000)
account2.show()  # ✅ แสดงชื่อบัญชี
#account2.deposit(5000)
#account2.withdraw(10000)

account1.tranfer(account2)

account2.showbalance()  # ✅ แสดงยอดเงินคงเหลือ



 
'''งงง
account1.show_other_account(account2)

print(account1.name)  
account1.showbalance() 
account1.oon_account(500, account2)

print(account1.name)  
account1.showbalance() 
account2.showbalance()
'''