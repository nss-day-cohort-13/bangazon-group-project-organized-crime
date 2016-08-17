from utility import *
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
        self.order_line_item_id = uuid.uuid4().int
        self.order_line_item_object = {"order_line_item_UUID": self.order_line_item_id,
                                       "order_UUID": self.order_UUID,
                                       "product_UUID": self.product_UUID}
        self.write_to_database()

# if __name__ == '__main__':
#     OrderLineItem.read_order_line_items()
