import unittest

from payment_options import *
from customer import *


class TestPaymentOptions(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.frankie = Customer("Frankie the Nose", "100 thief ave", "Bellvue", "TN", "37204", "615-867-5309")
        self.frankie_payment = Payment("visa", "123456789", self.frankie.customer_UUID)

    def test_payment_option_creation(self):
        self.assertEqual("visa", self.frankie_payment.payment_option_name)
        self.assertEqual("123456789", self.frankie_payment.payment_option_acc_number)
        self.assertEqual(self.frankie.customer_UUID, self.frankie_payment.customer_UUID)
        self.assertIsNotNone(self.frankie_payment.payment_option_UUID)


    def test_payment_option_retrieval(self):
        payments = Payment.read_payments()
        payment_type_list = []

        for payment_name in payments:
            payment_type_list.append(payment_name["payment option name"])
            payment_type_list.append(payment_name["payment account number"])
        self.assertIn("visa", payment_type_list)
        self.assertIn("123456789", payment_type_list)

if __name__ == '__main__':
    unittest.main()
