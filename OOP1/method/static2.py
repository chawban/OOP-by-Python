class Utility:
    @staticmethod
    def calculate_vat(amount, vat_rate=0.07):
        """คำนวณภาษีมูลค่าเพิ่ม (VAT)"""
        return amount * vat_rate

    @staticmethod
    def calculate_income_tax(income, tax_rate=0.15):
        """คำนวณภาษีเงินได้ (Income Tax)"""
        return income * tax_rate


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_total_price(self):
        """คำนวณราคาสินค้ารวม VAT"""
        vat = Utility.calculate_vat(self.price)
        return self.price + vat

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Total Price (incl. VAT): {self.get_total_price()}"


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_net_salary(self):
        """คำนวณเงินเดือนสุทธิหลังจากหักภาษีเงินได้"""
        tax = Utility.calculate_income_tax(self.salary)
        return self.salary - tax

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}, Net Salary (after tax): {self.get_net_salary()}"


# ทดสอบการทำงาน
if __name__ == "__main__":
    # สร้าง object ของ Product
    product = Product("Laptop", 30000)
    print(product)

    # สร้าง object ของ Employee
    employee = Employee("John Doe", 50000)
    print(employee)