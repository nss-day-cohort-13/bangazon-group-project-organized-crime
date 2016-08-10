from orders import *
from payment_options import *
from customer import *
from products import *
from order_line_item import *

class Crime:
    def __init__(self):
        self.active_user = ""
        self.payment_choice = ""
        self.payment_id = ""
        # self.payment_id = []
        self.product_list = ""
        self.active_order = ""


    # test, then logic, then menu, then files.

    def welcome_menu(self):
        # while True:
            print   (
                    '\n'
                    'THIS IS ORGANIZED CRIME, CAPICE?'
                    '\n' '\n'
                    'ARE YOU A MEMBER OF OUR THING?' '\n'
                    '\n' '\n'
                    '1. Yes' '\n'
                    '2. No'
                    '\n'
                    )

            reply = input("> ")
            if reply == '1':
                self.choose_active_member()
            if reply == '2':
                self.create_new_member()

    def choose_active_member(self):
        customer_list = Customer.read_customers()
        # print("customer list from function: ", customer_list)
        counter = 3
        print("1. Main Menu")
        print("2. Exit")
        for customer in customer_list:
            print(str(counter) + ". " + str(customer["name"]))
            counter += 1

        which = int(input("who you is? "))
        if which == 1:
            self.welcome_menu()
        if which == 2:
            exit()
        else:
            Crime.active_user = customer_list[(which - 3)]["customer_UUID"]

            new_order = Order(customer_list[(which - 3)]["customer_UUID"], 0)
            Crime.active_order = new_order.order_UUID
            # print("Welcome " + )
            self.show_products()

        # print(new_order.order_data)
        # print("active order", self.active_order)


    def create_new_member(self):
        # customer_address =
        # customer_city =
        # customer_state =
        # customer_zip =
        # customer_phone =
        print(
            '\n'
            'SO YOU WANNA MAKE YOUR BONES?'
            '\n' '\n'
            )

        customer_name = input("ENTER YOUR NAME > ")
        customer_street_address = input("ENTER YOUR STREET ADDRESS > ")
        customer_city = input("ENTER YOUR CITY > ")
        customer_state = input("ENTER YOUR STATE > ")
        customer_zip = input("ENTER YOUR ZIP CODE > ")
        customer_phone = input("ENTER YOUR PHONE NUMBER > ")

        new_customer = Customer(customer_name, customer_street_address, customer_city, customer_state, customer_zip, customer_phone)
        # print(new_customer.customer_object)
        new_order = Order(new_customer.customer_UUID, 0)
        Crime.active_order = new_order.order_UUID
        Crime.active_user = new_customer.customer_UUID
        print("your active user", Crime.active_user)
        self.show_products()


    def show_products(self):
        product_list = Product.read_products()
        counter = 4
        print("1. Checkout")
        print("2. Main Menu")
        print("3. Exit")
        for product in product_list:
            print(str(counter) + ". " + str(product["product_name"]))
            counter += 1
        which = int(input("what you want? "))
        if which == 1:
            Crime.show_order()
        elif which == 2:
            self.welcome_menu()
        elif which == 3:
            exit()
        elif which > 3:
            new_OLI = OrderLineItem(Crime.active_order, product_list[(which - 4)]["product_UUID"])
            self.show_products()
        else:
            print("something went wrong")
    def show_order():
        order_line_item_list = OrderLineItem.read_order_line_items()
        active_order_line_items = []
        product_list = Product.read_products()
        total_price = 0

        for OLI in order_line_item_list:
            if Crime.active_order == OLI["order_UUID"]:
                active_order_line_items.append(OLI)

        print("active OLI: ", active_order_line_items)


        for item in active_order_line_items:
            for product in product_list:
                if product['product_UUID'] == item['product_UUID']:
                    print(product["product_name"])
                    total_price += float(product["product_price"])
                print("you gotta pay: ", total_price)
        # print(new_OLI.order_line_item_object)
        # print(product_list[(which - 1)]["product_name"])

    def show_order():
            order_line_item_list = OrderLineItem.read_order_line_items()
            active_order_line_items = []
            product_list = Product.read_products()
            total_price = 0

            for OLI in order_line_item_list:
                if Crime.active_order == OLI["order_UUID"]:
                    active_order_line_items.append(OLI)

            print("active OLI: ", active_order_line_items)


            for item in active_order_line_items:
                for product in product_list:
                    if product['product_UUID'] == item['product_UUID']:
                        print(product["product_name"])
                        total_price += float(product["product_price"])
            print("you gotta pay: ", total_price)
            Crime.show_payments()


    def show_payments():
        payment_list = Payment.read_payments()
        active_user_payments = []
        for payment in payment_list:
            if Crime.active_user == payment["customer id"]:
                active_user_payments.append(payment)
        if len(active_user_payments) == 0:
            Crime.create_payment()

        counter = 1
        for payment in active_user_payments:

            print(str(counter) + ". " + str(payment["payment option name"]))
            counter += 1
        which = int(input("which card? "))
        Crime.active_payment = active_user_payments[(which - 1)]["payment option uuid"]
        print(Crime.active_payment)

    def create_payment():
        print(
            '\n'
            'BETTER HAVE MY MONEY!'
            '\n' '\n'
            )
        name = input("PAYMENT NAME > ")
        account = input("ACCOUNT NUMBER > ")
        new_payment = Payment(name, account, Crime.active_user)

#
#     def get_payment_options(self):
#         active_user_payments = []
#         all_payments = Payment.read_payments()
#         for payment in all_payments:
#             if self.active_user == payment["customer id"]:
#                 active_user_payments.append(payment)
#             else:
#                 # prompt to create payment option
#
#     def set_order_number(self):
#         if self.current_order = "" && self.active_user != "":
#             self.current_order_number = Customer(self.active_user, self.payment_id)
#         else:
#             print(self.current_order)


if __name__ == '__main__':
    crime = Crime()
    crime.welcome_menu()








    # def all_user_orders(self):
    #     active_user_past_orders = []
    #     all_orders = Orders.read_orders()
    #     for order in all_orders:
    #         if self.active_user == order["customer_UUID"]:
    #             active_user_past_orders.append(order])
    #
    # def list_line_item_products_with_prices(self):
    #     pass
