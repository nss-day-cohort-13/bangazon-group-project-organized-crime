import sqlite3

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
        self.order_UUID = None
        self.paid = 0
        self.order_data = {
                        "order_UUID": self.order_UUID,
                        "customer_UUID": self.customer_UUID,
                        "payment_UUID": self.payment_UUID,
                        "paid": self.paid
                        }
        self.write_to_order()

    def write_to_order(self):

        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

            c.execute("insert into Customer_order values(?,?,?,?)",
                     (
                     self.order_UUID,
                     self.customer_UUID,
                     self.payment_UUID,
                     self.paid
                     ))

            conn.commit()

    def read_orders():
        orders_list = []
        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

        for row in c.execute("SELECT * FROM Customer_order o"):
            orders_list.append(row)
        print(orders_list)
        return orders_list

    # @staticmethod
    # def read_orders():
    #     """ Deserializes all the pickled orders in the orders.txt file."""

    #     orders_deserialized = []
    #     with open("orders.txt", "rb+") as pickle_file:
    #         while True:
    #             try:
    #                 orders_deserialized.append(pickle.load(pickle_file))
    #             except FileNotFoundError:
    #                 print("I'm a potato!")
    #             except EOFError:
    #                 break
    #         print(orders_deserialized)
    #         return orders_deserialized

# if __name__ == '__main__':
#     # Order.read_orders()
#     new_order = Order(1,1)
#     Order.read_orders()
