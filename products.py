import uuid
import pickle

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

        self.serialize_product()

    def serialize_product(self):
        """
        This method uses pickle.dump to write and serialize product data and
        store it in the products.txt file.
        """

        with open ('products.txt', 'ab+') as pickle_products_file:
            pickle.dump(self.product_object, pickle_products_file)


    @staticmethod
    def read_products():
        """
        This method uses pickle.load to deserialize and read product data from
        the products.txt file.
        """
        product_list = []
        with open ('products.txt', 'rb') as pickle_products_file:
            while True:
                try:
                    product_list.append(pickle.load(pickle_products_file))
                except EOFError:
                    break

            # print(product_list)
            return product_list

# if __name__ == '__main__':
    # products = Product("brass knuckles", 19.99)
    # products = Product("spiked baseball bat", 36.99)
    # products = Product("piano wire (middle C)", 3.99)
