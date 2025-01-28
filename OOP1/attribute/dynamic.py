class Dog:
    pass

dog = Dog()
dog.name = "เจ้าตูบ"  # Dynamic Attribute
dog.age = 5         # Dynamic Attribute
print(dog.name)  # Output: เจ้าตูบ
print(dog.age)  # Output: เจ้าตูบ

#ควรใช้อย่างระมัดระวัง เพราะอาจทำให้โค้ดยากต่อการติดตามและดีบัก