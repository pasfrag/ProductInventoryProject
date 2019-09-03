from classes.product import Product


class Inventory:

    def __init__(self, product_dict, name):
        self.product_dict = product_dict
        self.name = name

    def add_product(self, product: Product):
        self.product_dict[product.product_id] = product

    def remove_product(self, product: Product):
        self.product_dict.pop(product.product_id)
