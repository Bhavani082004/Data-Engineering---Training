def calculate_total(price, quantity):
    return price * quantity
total = calculate_total(65000, 2)
print("Total Amount:", total)

def calculate_discount(amount):
    if amount >= 50000:
        return amount * 0.10
    else:
        return amount * 0.05
discount = calculate_discount(60000)
print("Discount:", discount)

def calculate_sales_total(sales):
    return sum(sales)
sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]
total_sales = calculate_sales_total(sales)
print("Total Sales:", total_sales)

def check_product(product):
    if product["stock"] > 0:
        return "Available"
    else:
        return "Out of Stock"

product1 = {
    "product_name": "Laptop",
    "stock": 12
}

product2 = {
    "product_name": "Monitor",
    "stock": 0
}
print(product1["product_name"], ":", check_product(product1))
print(product2["product_name"], ":", check_product(product2))
square = lambda number: number * number
print("Square:", square(5))

sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]
high_sales = list(filter(lambda sale: sale > 20000, sales))
print("Sales greater than 20000:", high_sales)

customers = [
    {"id": "C101", "name": "North Star Retail", "city": "Hyderabad"},
    {"id": "C102", "name": "Blue Mart", "city": "Mumbai"},
    {"id": "C103", "name": "Daily Basket", "city": "Bangalore"},
    {"id": "C104", "name": "Prime Stores", "city": "Hyderabad"}
]
cities = list(map(lambda customer: customer["city"], customers))
print("Customer Cities:", cities)

products = [
    {"product_name": "Laptop", "price": 65000},
    {"product_name": "Monitor", "price": 18000},
    {"product_name": "Office Chair", "price": 9000},
    {"product_name": "Keyboard", "price": 3000}
]

sorted_products = sorted(products, key=lambda product: product["price"])
print("Products sorted by price:")
for product in sorted_products:
    print(product["product_name"], "-", product["price"])
    