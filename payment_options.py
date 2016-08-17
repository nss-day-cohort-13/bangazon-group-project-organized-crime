import sqlite3

from customer import *

class Payment():

    def __init__(self,
        payment_name,
        payment_acc_number,
        customer_id):

        self.payment_option_name = payment_name
        self.payment_option_acc_number = payment_acc_number
        self.customer_UUID = customer_id
        self.payment_option_UUID = None
        self.payment_option_object = {"payment option name": self.payment_option_name,
                                      "payment account number": self.payment_option_acc_number,
                                      "customer id": self.customer_UUID,
                                      "payment option uuid": self.payment_option_UUID
                                      }
        self.write_to_payment()

    def write_to_payment(self):

        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

        c.execute("insert into payment values(?,?,?,?)",
                 (self.payment_option_UUID,
                  self.payment_option_name,
                  self.payment_option_acc_number,
                  self.customer_UUID)
                 )

        conn.commit()

    def read_payments():
        payment_list = []
        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

            for row in c.execute("""SELECT * FROM Payment"""):
                payment_list.append(row)
            print(payment_list)
            return payment_list





if __name__ == '__main__':
    new_payment = Payment('vias', '1234567', 1)
    Payment.read_payments()
