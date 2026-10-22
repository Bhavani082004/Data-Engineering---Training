def calculate_shipping_cost(weight, rate):
    return weight * rate


def shipment_category(weight):
    if weight > 20:
        return "Heavy"
    elif weight >= 10:
        return "Medium"
    else:
        return "Light"


def display_shipment(shipment_id, destination, weight, cost):
    print("Shipment ID:", shipment_id)
    print("Destination:", destination)
    print("Weight:", weight)
    print("Cost:", cost)