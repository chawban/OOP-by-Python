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

    # ✅ แก้ไขเมธอด show() และ showbalance() ให้ถูกต้อง
    def show(self):
        """ แสดงชื่อบัญชี """
        print(f"ชื่อบัญชี: {self.name}")

    def showbalance(self):
        """ แสดงยอดเงินคงเหลือ โดยใช้ get_balance() """
        print(f"ยอดเงินคงเหลือ: {self.get_balance()} บาท")
 
  
    def get_balance(self):
        """ เมธอดสำหรับตรวจสอบยอดเงินคงเหลือ """
        return self.__balance  # คืนค่าจำนวนเงินที่ซ่อนอยู่
           
    def show_other_account(self,target_account): 
        print(f"ชื่อบัญชีเราคือ: {self.name} ชื่อบัญชีคุณคือ {target_account.name}")


# ------------------ ตัวอย่างการใช้งาน ------------------ #

# สร้างบัญชีใหม่
account1 = BankAccount("Somsee RukGung", 1000)
account1.show()  # ✅ แสดงชื่อบัญชี
account1.showbalance()  # ✅ แสดงยอดเงินคงเหลือ
 
account2 = BankAccount("SomKhuan Narak", 55000)

#print(account1.name)  
#print(account1.__balance)  

print(account1.show_other_account(account2))
