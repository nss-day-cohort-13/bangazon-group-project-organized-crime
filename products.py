import uuid
from utility import *
class Product:
    """
    The Product class stores the UUID, name, and unit price of products.

    Methods on this class:
        __init__()
        serailize_product()
        read_products()
    """
    def __init__(self, name_of_product, unit_cost_of_product):
        self.unpickled_product_data = []
        self.product_UUID = uuid.uuid4().int
        self.name_of_product = name_of_product
        self.unit_cost_of_product = unit_cost_of_product

        self.product_object =   {
                                'product_UUID': self.product_UUID,
                                'product_name': self.name_of_product,
                                'product_price': self.unit_cost_of_product
                                }

        self.write_to_database()

# if __name__ == '__main__':
    # products = Product("brass knuckles", 19.99)
    # products = Product("spiked baseball bat", 36.99)
    # products = Product("piano wire (middle C)", 3.99)
