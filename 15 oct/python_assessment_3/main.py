import event_utils

amount = event_utils.calculate_booking_amount(5000, 2)
print("Booking Amount:", amount)

discount = event_utils.calculate_discount(amount)
print("Discount:", discount)

status = event_utils.check_event_capacity(500, 350)
print("Event Status:", status)

from event_utils import calculate_booking_amount
print("Direct Import:", calculate_booking_amount(3000, 3))

import event_utils as eu
print("Alias Import:", eu.calculate_discount(12000))
