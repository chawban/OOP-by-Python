class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# การเรียกใช้ static method
result_add = MathOperations.add(5, 3)       # ผลลัพธ์: 8
result_multiply = MathOperations.multiply(4, 2) # ผลลัพธ์: 8

print(result_add)
print(result_multiply)
