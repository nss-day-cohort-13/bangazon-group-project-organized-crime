import uuid
from utility import *
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
        self.write_to_database()

    # if __name__ == '__main__':
    # unittest.main()
