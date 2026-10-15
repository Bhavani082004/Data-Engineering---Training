import csv

with open("registrations.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    registrations = list(reader)

for registration in registrations:
    if registration["status"] == "Confirmed":
        print(registration)

for registration in registrations:
    if registration["city"] == "Hyderabad":
        print(registration)

for registration in registrations:
    registration["amount"] = float(registration["amount"])

for registration in registrations:
    if registration["amount"] > 7000:
        print(registration)

total_amount = sum(registration["amount"] for registration in registrations)
print("Total Registration Amount:", total_amount)

cities = [registration["city"] for registration in registrations]
unique_cities = set(cities)
print("Unique Cities:", unique_cities)
