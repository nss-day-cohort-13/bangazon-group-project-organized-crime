import pickle
import uuid

class OrderLineItem:


    def __init__(self, order_ID, product_ID):
        self.order_UUID = order_ID
        self.product_UUID = product_ID
        self.order_line_item_id = uuid.uuid4().int
        self.order_line_item_object = {"order_line_item_UUID": self.order_line_item_id,
                                       "order_UUID": self.order_UUID,
                                       "product_UUID": self.product_UUID}
        self.serialize()

    def serialize(self):
        with open('order_line_items.txt', 'ab+') as file:
            pickle.dump(self.order_line_item_object, file)

    @staticmethod
    def read_order_line_items():
        order_line_items_list = []
        with open('order_line_items.txt', 'rb') as file:
            while True:
                try:
                    order_line_items_list.append(pickle.load(file))
                except EOFError:
                    break

            print(order_line_items_list)
            return order_line_items_list






if __name__ == '__main__':
    OrderLineItem.read_order_line_items()

