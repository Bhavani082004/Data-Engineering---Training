with open("activity.txt", "w") as file:
    file.write("Processing started.\n")
    file.write("Customer records loaded.\n")
    file.write("Product records loaded.\n")

print("Three messages written successfully.")

with open("activity.txt", "a") as file:
    file.write("Processing completed successfully.\n")

print("Additional message appended successfully.")
with open("activity.txt", "r") as file:
    content = file.read()
print(content)
import csv
with open("data/customers.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    customers = list(reader)
print("All Customer Records:")
print(customers)

print("\nActive Customers:")

for customer in customers:
    if customer["active"].strip().lower() == "true":
        print(customer["customer_name"])

print("\nHyderabad Customers:")

for customer in customers:
    if customer["city"].strip().lower() == "hyderabad":
        print(customer["customer_name"])
import json
with open("data/products.json", "r", encoding="utf-8") as file:
    products = json.load(file)

print("All Product Records:")
print(products)
print("\nAll Product Names:")
for product in products:
    print(product["product_name"])
print("\nProducts Costing Above 10000:")

for product in products:
    if product["price"] > 10000:
        print(product)
print("\nProducts Costing Above 10000:")

print("\nSupplier Name and City:")
for product in products:
    supplier = product["supplier"]
    print("Supplier Name:", supplier["name"])
    print("Supplier City:", supplier["city"])
all_colors = []

for product in products:
    all_colors.extend(product["colors"])
    print("\nAll Colors:")
    print(all_colors)
unique_colors = set(all_colors)
print("\nUnique Colors:")
print(unique_colors)
for product in products:
    if product["product_id"] == 202:
        product["stock"] += 1
        print("\nUpdated Product:")
        print(product)
        break

with open("data/products_updated.json", "w", encoding="utf-8") as file:
    json.dump(products, file, indent=4)
    print("\nUpdated data saved to products_updated.json")
