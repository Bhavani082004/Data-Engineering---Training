product_name = input("Enter product name: ")
unit_price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity: "))

total_amount = unit_price * quantity

if total_amount >= 50000:
    discount = total_amount * 0.10
else:
    discount = total_amount * 0.05

final_amount = total_amount - discount

print("\n========== ORDER DETAILS ==========")
print(f"Product Name: {product_name}")
print(f"Unit Price: ₹{unit_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Original Amount: ₹{total_amount:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")


stock = int(input("Enter stock quantity: "))

if stock > 20:
    print("High Stock")
elif stock >= 1:
    print("Low Stock")
else:
    print("Out of Stock")

for number in range(1, 11):
    print(number)
print("\n========== STOCK COUNTDOWN ==========")
stock = 5
while stock >= 0:
    print("Stock:", stock)
    stock -= 1
print("\n========== SKIP NUMBER 5 ==========")
for number in range(1, 11):
    if number == 5:
        continue
    print(number)
print("\n========== STOP AT NUMBER 8 ==========")
for number in range(1, 11):
    if number == 8:
        break
    print(number)