import pickle
import uuid

class OrderLineItem:


    def __init__(self, order_ID, product_ID):
        self.order_UUID = order_ID
        self.product_UUID = product_ID
        self.order_line_item_id = uuid.uuid4().int





# if __name__ == '__main__':


