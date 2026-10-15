attendee_name = input("Enter attendee name: ")
tickets = int(input("Enter number of tickets: "))
ticket_price = float(input("Enter ticket price: "))

total_amount = tickets * ticket_price

if total_amount >= 10000:
    discount = total_amount * 0.10
else:
    discount = total_amount * 0.05

final_amount = total_amount - discount

print(f"Attendee Name: {attendee_name}")
print(f"Number of Tickets: {tickets}")
print(f"Ticket Price: ₹{ticket_price:.2f}")
print(f"Total Booking Amount: ₹{total_amount:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")

capacity = int(input("Enter event capacity: "))
registered = int(input("Enter registered participants: "))

if registered == capacity:
    print("Full")
elif registered < capacity:
    print("Seats Available")
else:
    print("Invalid Data")

for i in range(1, 16):
    if i % 3 == 0:
        print(i)

count = 10

while count >= 1:
    print(count)
    count -= 1

print("Break")

for i in range(1, 11):
    if i == 6:
        break
    print(i)

print("Continue")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)











