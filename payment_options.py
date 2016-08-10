import uuid
import pickle

from customer import *

class Payment():
    def __init__(self,
        payment_name,
        payment_acc_number,
        customer_id):
        '''
         On initialization of the Payment Class, this function takes the payment_name, payment_account number and the customer id, and
         assigns them to variables for this instance. Variables are combined to define one payment option object.
         Customer id is created using the uuid module.
         The serialize_payment function is called here.


         arguments: payment_name , payment account number, customer id

        '''

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
         """
        This function uses the pickle module to append payment option data to the payments.txt file

        arguments: none
        """
        with open('payments.txt', 'ab+') as file:
            pickle.dump(self.payment_option_object, file)


    @staticmethod
    def read_payments():
         """
        This function uses the pickle module to retrieve payment option data in the payments.txt file

        arguments: none
        """

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







