import sqlite3
import uuid

class OrderLineItem:
    '''
    Creates a order line item object, used to associate multiple product
    ID numbers with a single order ID number, creating the relationship between
    adding products to an order

    keyword arguments:
    order_ID: derived from active order
    product_ID: derived from products that are added to the active order
    '''


    def __init__(self, order_ID, product_ID):
        self.order_UUID = order_ID
        self.product_UUID = product_ID
        self.order_line_item_id = None
        self.order_line_item_object = {"order_line_item_UUID": self.order_line_item_id,
                                       "order_UUID": self.order_UUID,
                                       "product_UUID": self.product_UUID}
        self.write_to_order_line_items()

    def write_to_order_line_items(self):
      with sqlite3.connect('bangazon.db') as conn:
        c = conn.cursor()

        c.execute("insert into Order_line_item values(?, ?, ?)",
                  (self.order_line_item_id, self.order_UUID, self.product_UUID))

        conn.commit()

    @staticmethod
    def read_order_line_items():
      order_line_item = []
      with sqlite3.connect('bangazon.db') as conn:
        c = conn.cursor()

      for row in c.execute("SELECT * FROM Order_line_item oli"):
        order_line_item.append(row)

      print(order_line_item)
      return order_line_item






if __name__ == '__main__':
    OrderLineItem(234324235, 235436346356)
    OrderLineItem.read_order_line_items()
