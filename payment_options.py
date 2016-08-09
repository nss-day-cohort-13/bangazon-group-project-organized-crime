import uuid
import pickle

from customer import *

class Payment():

    def __init__(self,
        payment_name,
        payment_acc_number,
        customer_id):

        self.payment_option_name = payment_name
        self.payment_option_acc_number = payment_acc_number
        self.customer_UUID = customer_id
        self.payment_option_UUID = uuid.uuid4().int
        self.payment_option_object = {"payment option name": self.payment_option_name,
                                      "payment account number": self.payment_option_acc_number,
                                      "customer id": self.customer_UUID,
                                      "payment option uuid": self.payment_option_UUID
                                      }
        self.serialize_payment()

    def serialize_payment(self):
        with open('payments.txt', 'ab+') as file:
            pickle.dump(self.payment_option_object, file)


    @staticmethod
    def read_payments():
        payment_option_list = []
        with open('payments.txt', 'rb+') as file:
            while True:
                try:
                    payment_option_list.append(pickle.load(file))
                except  EOFError:
                    break
            print(payment_option_list)
            return payment_option_list




    # if __name__ == '__main__':
    # unittest.main()







