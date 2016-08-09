import unittest

from payment_options import *
from customer import *
from orders import *


class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.frankie = Customer("Frankie the Nose", "100 thief ave", "Bellvue", "TN", "37204", "615-867-5309")
        self.frankie_payment = Payment("visa", "123456789", self.frankie.customer_UUID)
        self.frankie_order = Order(self.frankie.customer_UUID, self.frankie_payment.payment_option_UUID)

    def test_order_creation(self):
        self.assertEqual(self.frankie_order.customer_UUID, self.frankie.customer_UUID)
        self.assertEqual(self.frankie_order.payment_UUID, self.frankie_payment.payment_option_UUID)
        self.assertEqual(self.frankie.customer_UUID, self.frankie_payment.customer_UUID)
        self.assertFalse(self.frankie_order.paid)
        self.assertIsNotNone(self.frankie_order.order_UUID)


    # def test_order_retrieval(self):
    #     orders = Order.read_orders()
    #     order_list = []

    #     for order in orders:
    #         order_list.append(order[self.frankie_order.order_UUID])
    #         order_list.append(order[self.frankie_order.customer_UUID])
    #     self.assertEqual(self.frankie_order.customer_UUID, self.frankie.customer_UUID )
    #     self.assertEqual(self.frankie_order.payment_UUID, self.frankie_payment.payment_UUID)

if __name__ == '__main__':
    unittest.main()
