class Product:

    def __init__(self, name, product_id, quantity, price):
        self.name = name
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def update_product(self, name=None, product_id=None, quantity=None, price=None):
        if name:
            self.name = name
        if product_id:
            self.product_id = product_id
        if quantity:
            self.quantity = quantity
        if price:
            self.price = price
