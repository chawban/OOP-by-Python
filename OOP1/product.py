# Procedural Approach
products = []

def add_product(name, price):
    products.append({"name": name, "price": price})

def remove_product(name):
    global products
    products = [product for product in products if product["name"] != name]

def show_products():
    for product in products:
        print(f"Product: {product['name']}, Price: {product['price']}")

# การใช้งาน
add_product("Laptop", 30000)
add_product("Mouse", 500)
show_products()
remove_product("Mouse")
show_products()
