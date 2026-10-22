import csv
import json
import os

project_folder = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(project_folder, "data")


with open(os.path.join(data_folder, "customers.csv"), "r", newline="") as file:
    customers = list(csv.DictReader(file))

print("CUSTOMERS DATA")
print("Total customers:", len(customers))
print(customers[0])


with open(os.path.join(data_folder, "orders.csv"), "r", newline="") as file:
    orders = list(csv.DictReader(file))

print("\nORDERS DATA")
print("Total orders:", len(orders))
print(orders[0])

with open(os.path.join(data_folder, "products.json"), "r") as file:
    products = json.load(file)

print("\nPRODUCTS DATA")
print("Total products:", len(products))
print(products[0])

import retail_utils
total = retail_utils.calculate_order_total(2000, 10)
print("Order Total:", total)
discount = retail_utils.calculate_discount(total)
print("Discount:", discount)
stock_status = retail_utils.check_stock(10)
print("Stock Status:", stock_status)

from retail_utils import calculate_order_total

total_amount = calculate_order_total(1500, 4)

print("Direct Import Order Total:", total_amount)

import retail_utils as ru

alias_total = ru.calculate_order_total(3000, 5)
print("Alias Order Total:", alias_total)

alias_discount = ru.calculate_discount(alias_total)
print("Alias Discount:", alias_discount)

alias_stock = ru.check_stock(0)
print("Alias Stock Status:", alias_stock)