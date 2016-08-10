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
            self.active_customer = customer_list[(which - 1)]["customer_UUID"]
            # print(self.active_customer)

            new_order = Order(customer_list[(which - 1)]["customer_UUID"], 0)
            self.active_order = new_order.order_UUID
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
        print(new_customer.customer_object)

        self.show_products()


    def show_products(self):
        print("Here are your products")

#             user_full_name = input(">")
#             # store in memory, then
#
#             print   (
#                     "Please Enter the New User's Screen Name"
#                     "\n" "\n"
#                     )
#
#             user_screen_name = input(">")
#
#         elif selection == '2':
#             print ("Who would you like to pretend you are today?")
#             # print list of user names from user_data.txt
#             input (">")
#
#         elif selection == '3':
#             print   (
#                     "\n"
#                     "View All Chirps" "\n" "\n"
#                     "1. View all private Chirps." "\n"
#                     "2. View all public Chirps."
#                     )
#             input (">")
#
#         #     if selection == '1':
#         #         # goto list of users with whom this user has private Chirps
#         #     elif selection == '2':
#         #         # goto chronological list of all public chirps.
#         #         #   Hmm...chronological by first Chirp or by most recent reply?)
#         #     else print ("You don't know what you want.")
#
#         # elif selection == '4':
#         #     print ("You Can Make A New Public Chirp!")
#         #     print ("No, go ahead;  We're all so interested in what you have to say.")
#         #     print ("")
#         #     input (">")
#
#         elif selection == '5':
#             print ("You Can Make A New Private Chirp!")
#             print ("From which user do you desperately crave attention," \
#                     " you very lonely person?")
#             print ("")
#             # print (numbered userlist)
#             print ("")
#             input (">")
#
#         elif selection == '6':
#             print   ("Yes!  Go outside; play in the rain." "\n"
#                     "Love yourself more than this.")
#
#         else:
#             print ("You want the impossible.")
#             main_menu()
#
# main_menu()
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
