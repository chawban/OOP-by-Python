# สร้าง list เก็บผลไม้
fruits = []

# เพิ่มผลไม้ 10 รายการลงใน list
fruits.append("Apple")
fruits.append("Banana")
fruits.append("Orange")
fruits.append("Mango")
fruits.append("Grapes")
fruits.append("Pineapple")
fruits.append("Watermelon")
fruits.append("Strawberry")
fruits.append("Papaya")
fruits.append("Cherry")

fruits.remove("Grapes")

# แสดงผลไม้ทั้งหมดใน list
print("Fruits in the basket:")
for fruit in fruits:
    print(fruit)
