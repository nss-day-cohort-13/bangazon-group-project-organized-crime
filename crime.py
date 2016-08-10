from orders import *
from payment_options import *
from customer import *

class Crime:
    def __init__(self):
        self.active_user = ""
        self.payment_choice = ""
        self.product_list = ""

    def get_payment_options(self):
        active_user_payments = []
        all_payments = Payment.read_payments()
        for payment in all_payments:
            if self.active_user == payment["customer id"]:
                active_user_payments.append(payment[payment])

    # def set_payment_type(self):
    #     pass

    def order(self):
        pass

    def line_items(self):
        pass
