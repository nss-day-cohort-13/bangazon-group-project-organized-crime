from orders import *
from payment_options import *
from customer import *

class Crime:
    def __init__(self):
        self.active_user = ""
        self.payment_choice = ""
        self.payment_id = ""
        # self.payment_id = []
        self.product_list = ""
        self.current_order_number = ""

    def get_payment_options(self):
        active_user_payments = []
        all_payments = Payment.read_payments()
        for payment in all_payments:
            if self.active_user == payment["customer id"]:
                active_user_payments.append(payment)
            else:
                # prompt to create payment option

    def set_order_number(self):
        if self.current_order = "" && self.active_user != "":
            self.current_order_number = Customer(self.active_user, self.payment_id)
        else:
            print(self.current_order)

    def all_user_orders(self):
        active_user_past_orders = []
        all_orders = Orders.read_orders()
        for order in all_orders:
            if self.active_user == order["customer_UUID"]:
                active_user_past_orders.append(order])

    def list_line_item_products_with_prices(self):
        pass
