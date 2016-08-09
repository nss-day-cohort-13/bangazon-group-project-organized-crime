import pickle
import uuid

class Order:
    """ Creates new orders and reads orders that were created. """
    def __init__(self):
        """ Holds unpickled data """
        self.orders_deserialized = []

    def create_order(self, customer_id, payment_id):
        """ Writes a new order to the orders.txt CSV file.

        Keyword arguements:
        customer_id -- the id of the customer creating the order_id
        payment_id -- id of the payment that the customer chose to use
        Uses the pickle module to serialize data from the CSV file.
         """
        order_id = uuid.uuid4().int
        try:
            self.read_orders()
        except EOFError:
            pass
        except FileNotFoundError:
            print("I'm a potato!")

        with open("orders.txt", "wb+") as pickle_file:
            order_data = {
                "order_UUID": order_id,
                "customer_UUID": customer_id,
                "payment_UUID": payment_id,
                "paid": False
            }
            self.orders_deserialized.append(order_data)
            pickle.dump(self.orders_deserialized, pickle_file)

    def read_orders(self):
        """ Reads all the orders in the orders.txt CSV file.

        Keyword arguments: None
        Uses the pickle module to deserialize data from the csv file.
         """
        with open("orders.txt", "rb+") as pickle_file:
            self.orders_deserialized = pickle.load(pickle_file)
            print(self.orders_deserialized)
            return self.orders_deserialized

if __name__ == '__main__':
    order = Order()
    # order.create_order(1234, 4567)
    order.read_orders()
