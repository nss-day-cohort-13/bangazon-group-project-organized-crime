import sqlite3

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
        self.product_UUID = None
        self.name_of_product = name_of_product
        self.unit_cost_of_product = unit_cost_of_product

        # self.product_object =   {
        #                         'product_UUID': self.product_UUID,
        #                         'product_name': self.name_of_product,
        #                         'product_price': self.unit_cost_of_product
        #                         }

        self.write_to_product()


    def write_to_product(self):

        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

            c.execute("insert into product values(?,?,?)",
                (self.product_UUID,
                 self.name_of_product,
                 self.unit_cost_of_product))

            conn.commit()

    def




    # @staticmethod
    # def read_products():
    #     """
    #     This method uses pickle.load to deserialize and read product data from
    #     the products.txt file.
    #     """
    #     product_list = []
    #     with open ('products.txt', 'rb') as pickle_products_file:
    #         while True:
    #             try:
    #                 product_list.append(pickle.load(pickle_products_file))
    #             except EOFError:
    #                 break

    #         # print(product_list)
    #         return product_list

# if __name__ == '__main__':
#     products = Product("brass knuckles", 19.99)
#     products = Product("spiked baseball bat", 36.99)
#     products = Product("piano wire (middle C)", 3.99)
