from utility import *
import uuid

class Order:
    """
    Creates new orders and reads all orders that have been created.

    Methods on class:
      create_order()
      read_orders()
    """
    def __init__(self, customer_id, payment_id):
        """
        Creates an order with a unique order id(UUID module), the id of the
        active customer, and the id of the payment chosen by the user.

        Keyword Arguments:
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
        self.write_to_database()

if __name__ == '__main__':
    Order.read_orders()
    # Order(1234435345345, 937924837928)
