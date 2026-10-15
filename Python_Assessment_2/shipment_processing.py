weight = float(input("Enter shipment weight (kg): "))
cost = float(input("Enter shipment cost: "))

cost_per_kg = cost / weight
print("Cost per kg:", round(cost_per_kg, 2))

if weight > 20:
    print("Category: Heavy")
elif weight >= 10:
    print("Category: Medium")
else:
    print("Category: Light")

print("Shipment numbers from 1 to 20:")
for i in range(1, 21):
    print(i)

print("Even shipment numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("Processing attempts:")
attempt = 1
while attempt <= 5:
    print("Processing attempt", attempt)
    attempt += 1

shipment_costs = [850, 620, 1250, 480, 1600, 740, 590, 1100, 920, 1750, 520, 1050]

print("Shipment costs:", shipment_costs)

print("Total cost:", sum(shipment_costs))
print("Average cost:", sum(shipment_costs) / len(shipment_costs))
print("Minimum cost:", min(shipment_costs))
print("Maximum cost:", max(shipment_costs))

destinations = [
"Hyderabad", "Mumbai", "Bangalore", "Delhi",
"Pune", "Hyderabad", "Mumbai", "Delhi",
"Bangalore", "Pune", "Hyderabad", "Mumbai"
]

unique_destinations = set(destinations)
print("Unique destinations:", unique_destinations)

shipment = {
"shipment_id": "S1001",
"hub_id": "H01",
"destination": "Hyderabad",
"weight": 12.5,
"status": "Delivered",
"cost": 850
}

print("One shipment:", shipment)

shipments = [
{"shipment_id": "S1001", "destination": "Hyderabad", "status": "Delivered", "cost": 850},
{"shipment_id": "S1002", "destination": "Mumbai", "status": "In Transit", "cost": 620},
{"shipment_id": "S1003", "destination": "Bangalore", "status": "Delivered", "cost": 1250},
{"shipment_id": "S1004", "destination": "Delhi", "status": "Pending", "cost": 480}
]

print("Multiple shipments:")
for item in shipments:
    print(item)

print("Delivered shipments:")
for item in shipments:
    if item["status"] == "Delivered":
        print(item)

def calculate_shipping_cost(weight, rate):
    return weight * rate
print("Shipping cost:", calculate_shipping_cost(12.5, 50))

def shipment_category(weight):
    if weight > 20:
        return "Heavy"
    elif weight >= 10:
        return "Medium"
    else:
        return "Light"

print("Shipment category:", shipment_category(12.5))

delivered_shipments = list(filter(lambda x: x["status"] == "Delivered", shipments))
print("Delivered shipments:", delivered_shipments)

all_destinations = list(map(lambda x: x["destination"], shipments))
print("All destinations:", all_destinations)

sorted_shipments = sorted(shipments, key=lambda x: x["cost"])

print("Shipments sorted by cost:")
for item in sorted_shipments:
    print(item)

class Shipment:
    def __init__(self, shipment_id, destination, weight, cost):
        self.shipment_id = shipment_id
        self.destination = destination
        self.weight = weight
        self.cost = cost

    def calculate_cost(self):
        return self.cost

    def display(self):
        print("Shipment ID:", self.shipment_id)
        print("Destination:", self.destination)
        print("Weight:", self.weight)
        print("Cost:", self.calculate_cost())


class ExpressShipment(Shipment):
    def __init__(self, shipment_id, destination, weight, cost, surcharge):
        super().__init__(shipment_id, destination, weight, cost)
        self.surcharge = surcharge

    def calculate_cost(self):
        return self.cost + self.surcharge


normal_shipment = Shipment("S1001", "Hyderabad", 12.5, 850)
express_shipment = ExpressShipment("S1002", "Mumbai", 8.0, 620, 200)

print("Normal Shipment:")
normal_shipment.display()

print("\nExpress Shipment:")
express_shipment.display()

print("\nPolymorphism:")
for shipment in [normal_shipment, express_shipment]:
    print(shipment.shipment_id, "Final Cost:", shipment.calculate_cost())

import json

with open("employees.json", "r") as file:
    employees = json.load(file)

print("Employee Names:")
for employee in employees:
    print(employee["name"])

print("\nEmployees earning above 75000:")
for employee in employees:
    if employee["salary"] > 75000:
        print(employee["name"], employee["salary"])

print("\nEmployees knowing Python:")
for employee in employees:
    if "Python" in employee["skills"]:
        print(employee["name"])


print("\nEmployee Performance Ratings:")
for employee in employees:
    print(employee["name"], employee["performance"]["rating"])


print("\nEmployees with rating above 4.5:")
for employee in employees:
    if employee["performance"]["rating"] > 4.5:
        print(employee["name"])


sorted_employees = sorted(
    employees,
    key=lambda employee: employee["performance"]["rating"],
    reverse=True
)

print("\nEmployees sorted by rating:")
for employee in sorted_employees:
    print(employee["name"], employee["performance"]["rating"])


for employee in employees:
    if employee["employee_id"] == 303:
        employee["skills"].append("Python")


with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

print("\nUpdated employees.json successfully.")