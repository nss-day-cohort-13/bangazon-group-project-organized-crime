import pickle
import uuid

class Order:
    """ Creates new orders and reads orders that were created. """
    def __init__(self, customer_id, payment_id):
        """  """
        self.customer_UUID = customer_id
        self.payment_UUID = payment_id
        self.order_UUID = uuid.uuid4().int
        self.paid = False
        self.order_data = {
                        "order_UUID": self.order_UUID,
                        "customer_UUID": self.customer_UUID,
                        "payment_UUID": self.payment_UUID,
                        "paid": self.paid
                        }
        self.create_order()

    def create_order(self):
        """ Writes a new order to the orders.txt CSV file.

        Keyword arguements:
        customer_id -- the id of the customer creating the order_id
        payment_id -- id of the payment that the customer chose to use
        Uses the pickle module to serialize data from the CSV file.
         """

        with open("orders.txt", "ab+") as pickle_file:
            pickle.dump(self.order_data, pickle_file)

    @staticmethod
    def read_orders():
        """ Reads all the orders in the orders.txt CSV file.

        Keyword arguments: None
        Uses the pickle module to deserialize data from the csv file.
         """
        orders_deserialized = []
        with open("orders.txt", "rb+") as pickle_file:
            while True:
                try:
                    orders_deserialized.append(pickle.load(pickle_file))
                except FileNotFoundError:
                    print("I'm a potato!")
                except EOFError:
                    break
            print(orders_deserialized)
            return orders_deserialized

if __name__ == '__main__':
    Order.read_orders()
    # Order(1234435345345, 937924837928)
