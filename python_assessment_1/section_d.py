class Product:
    def __init__(self, product_id, product_name, price, stock):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.stock = stock

    def display_product(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Stock:", self.stock)

    def calculate_value(self):
        return self.price * self.stock
product1 = Product(201, "Laptop", 65000, 12)
product2 = Product(202, "Monitor", 18000, 8)
product1.display_product()
print("Stock Value:", product1.calculate_value())
print()
product2.display_product()
print("Stock Value:", product2.calculate_value())
class DiscountedProduct(Product):
    def __init__(self, product_id, product_name, price, stock, discount_percent):
        super().__init__(product_id, product_name, price, stock)
        self.discount_percent = discount_percent

    def display_product(self):
        super().display_product()
        print("Discount:", self.discount_percent, "%")
discounted_product = DiscountedProduct(
    203, "Office Chair", 9000, 15, 10
)

discounted_product.display_product()
class PremiumProduct(Product):
    def display_product(self):
        print("=== PREMIUM PRODUCT ===")
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Stock:", self.stock)
        print("Category: Premium")
premium_product = PremiumProduct(204, "Keyboard", 3000, 30)
premium_product.display_product()
products = [
    Product(201, "Laptop", 65000, 12),
    DiscountedProduct(203, "Office Chair", 9000, 15, 10),
    PremiumProduct(204, "Keyboard", 3000, 30)
]
for product in products:
    product.display_product()
    print()