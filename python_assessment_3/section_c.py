def calculate_booking(ticket_price, tickets):
    return ticket_price * tickets



def calculate_discount(amount):
    if amount >= 10000:
        return amount * 0.10
    return amount * 0.05



def is_registration_active(status):
    return status == "Confirmed"



def calculate_total(amounts):
    return sum(amounts)



increase_amount = lambda amount: amount * 1.10



booking_amounts = [5000, 3500, 7500, 6000, 4000, 7000, 3000, 10000]
amounts_above_6000 = list(filter(lambda amount: amount > 6000, booking_amounts))
print(amounts_above_6000)



registrations = [
    {"registration_id": "R1001", "attendee_name": "Aarav Shah", "city": "Hyderabad", "status": "Confirmed", "amount": 5000},
    {"registration_id": "R1002", "attendee_name": "Simran Kaur", "city": "Mumbai", "status": "Confirmed", "amount": 3500},
    {"registration_id": "R1003", "attendee_name": "Faiz Ahmed", "city": "Pune", "status": "Pending", "amount": 7500},
    {"registration_id": "R1004", "attendee_name": "Keerthi Rao", "city": "Bangalore", "status": "Confirmed", "amount": 6000}
]

confirmed_registrations = list(filter(lambda registration: registration["status"] == "Confirmed", registrations))
print(confirmed_registrations)


attendee_cities = list(map(lambda registration: registration["city"], registrations))
print(attendee_cities)

unique_cities = set(map(lambda registration: registration["city"], registrations))
print(unique_cities)

sorted_registrations = sorted(registrations, key=lambda registration: registration["amount"])
print(sorted_registrations)
