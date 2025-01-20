# OOP Approach
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]

    def show_products(self):
        for product in self.products:
            print(product)

# การใช้งาน
store = Store()
product1 = Product("Laptop", 30000)
product2 = Product("Mouse", 500)

store.add_product(product1)
store.add_product(product2)
store.show_products()
store.remove_product("Mouse")
store.show_products()
