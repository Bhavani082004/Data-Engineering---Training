import shipment_utils
from shipment_utils import calculate_shipping_cost

print(shipment_utils.shipment_category(25))
print(calculate_shipping_cost(12.5, 50))
shipment_utils.display_shipment("S1001", "Hyderabad", 12.5, 850)
