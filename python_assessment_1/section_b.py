sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]

total_sales = sum(sales)

print("Total Sales:", total_sales)

highest_sale = max(sales)
lowest_sale = min(sales)

print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)

print("Sales greater than 20000:")

for sale in sales:
    if sale > 20000:
        print(sale)

sales.sort(reverse=True)

print("Sales from highest to lowest:", sales)

cities = [
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Pune",
    "Mumbai"
]

unique_cities = set(cities)

print("Unique Cities:", unique_cities)

product = (201, "Laptop", "Electronics", 65000)

product_id, product_name, category, price = product

print("Product ID:", product_id)
print("Product Name:", product_name)
print("Category:", category)
print("Price:", price)

customer = {
    "id": "C101",
    "name": "North Star Retail",
    "city": "Hyderabad",
    "orders": 5,
    "active": True
}
print("Customer:", customer)

customer["city"] = "Chennai"
print("Updated City:", customer["city"])

customer["orders"] += 1
print("Updated Order Count:", customer["orders"])

customer["email"] = "northstar@example.com"

print("Updated Customer:", customer)

print("Customer Details:")

for key, value in customer.items():
    print(key, ":", value)
