import uuid
import pickle

class Products:

    def __init__(self):
        self.unpickled_product_data = []

    def createProduct(self, name_of_product, unit_cost_of_product):
        try:
            self.retrieveProduct()
        except EOFError:
            pass
        except FileNotFoundError:
            print('You want the impossible.')

        with open('products.txt', 'wb+') as pickle_products_file:
            products_data = {
                            'product_UUID': uuid.uuid4().int,
                            'product_name': name_of_product,
                            'product_price': unit_cost_of_product
                            }

            self.unpickled_product_data.append(products_data)
            pickle.dump(self.unpickled_product_data, pickle_products_file)


    def retrieveProduct(self):
        with open ('products.txt', 'rb+') as pickle_products_file:
            self.unpickled_product_data = pickle.load(pickle_products_file)
            print(self.unpickled_product_data)
            return self.unpickled_product_data

if __name__ == '__main__':
    products = Products()
    # products.createProduct('spiked baseball bat', 37.99)
    products.retrieveProduct()
