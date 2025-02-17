class BankAccount:
<<<<<<< HEAD
    def __init__(self,name, balance):
        self.name=name
        self.__balance = balance  # private attribute
        
=======
    def __init__(self, balance):
        self.__balance = balance  # private attribute
>>>>>>> d985458d0721adff89b07f5312a95c53ac062ed3
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance  # method to access private attribute

<<<<<<< HEAD

class abc:
    
    def xxx(self):
        b1 = BankAccount('B1', 5000)
        print(b1.name)
        print(b1.__balance)
        

#xyz = abc()
#xyz.xxx()
  
# การใช้
account = BankAccount('สมหมาย',1000) 

#account.__balance = 2000
#account._BankAccount__balance = 15000
print(account.get_balance())  # ออกมา 15000


 
account.deposit(500)
print(account.get_balance()) 
account.withdraw(200)
print(account.get_balance())   



'''
print(account.__balance)  # 1300

#การใช้ __ ทำให้ __balance เป็น private attribute โดย Python จะทำ name mangling เพื่อเปลี่ยนชื่อแอตทริบิวต์เป็น _BankAccount__balance
'''
=======
# การใช้
account = BankAccount(1000) 

account.__balance = 2000
account._BankAccount__balance = 15000
print(account.get_balance())  # ออกมา 15000

account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # 1300

print(account.__balance)  # 1300

#การใช้ __ ทำให้ __balance เป็น private attribute โดย Python จะทำ name mangling เพื่อเปลี่ยนชื่อแอตทริบิวต์เป็น _BankAccount__balance
>>>>>>> d985458d0721adff89b07f5312a95c53ac062ed3
