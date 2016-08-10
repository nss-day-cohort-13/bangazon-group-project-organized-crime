import pickle
import uuid

class Order:
    """ Creates new orders and reads all orders that have been created. """
    def __init__(self, customer_id, payment_id):
        """ Creates an order with a unique order id(UUID module), the id of the
        active customer, and the id of the payment chosen by the user.

        Arguments:
        customer_id = the UUID of the active customer_id
        payment_id = is 0 until the customer selects their payment option
         """
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
        """ Serializes a new order by pickling to the orders.txt file. """

        with open("orders.txt", "ab+") as pickle_file:
            pickle.dump(self.order_data, pickle_file)

    @staticmethod
    def read_orders():
        """ Deserializes all the pickled orders in the orders.txt file."""

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
