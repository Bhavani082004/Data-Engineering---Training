import json

with open("staff.json", "r", encoding="utf-8") as file:
    staff = json.load(file)

print(type(staff))

for employee in staff:
    print(employee["name"])

for employee in staff:
    if employee["department"] == "Operations":
        print(employee)

for employee in staff:
    if employee["salary"] > 75000:
        print(employee)

for employee in staff:
    if "Python" in employee["skills"]:
        print(employee)

for employee in staff:
    print("Name:", employee["name"])
    print("Rating:", employee["performance"]["rating"])
    print("Events Handled:", employee["performance"]["events_handled"])

for employee in staff:
    if employee["performance"]["rating"] > 4.5:
        print(employee)

all_skills = []

for employee in staff:
    all_skills.extend(employee["skills"])

print(all_skills)

unique_skills = set(all_skills)
print(unique_skills)

staff_by_salary = sorted(staff, key=lambda employee: employee["salary"], reverse=True)
print(staff_by_salary)

staff_by_rating = sorted(staff, key=lambda employee: employee["performance"]["rating"], reverse=True)
print(staff_by_rating)

for employee in staff:
    if employee["staff_id"] == 503:
        if "Pandas" not in employee["skills"]:
            employee["skills"].append("Pandas")

with open("staff_updated.json", "w", encoding="utf-8") as file:
    json.dump(staff, file, indent=4)
