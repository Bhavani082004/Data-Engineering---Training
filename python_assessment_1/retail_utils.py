def calculate_order_total(price, quantity):
    return price * quantity
def calculate_discount(total):
    if total >= 50000:
        return total * 0.10
    else:
        return total * 0.05
def check_stock(stock):
    if stock > 0:
        return "Product is in stock"
    else:
        return "Product is out of stock"