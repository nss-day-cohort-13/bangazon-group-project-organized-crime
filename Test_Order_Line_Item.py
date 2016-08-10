import unittest

from order_line_item import *
from customer import *
from orders import *
from products import *
from payment_options import *

class TestOrderLineItem(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.frankie = Customer("Frankie the Nose", "100 thief ave", "Bellvue", "TN", "37204", "615-867-5309")
        self.frankie_payment = Payment("visa", "123456789", self.frankie.customer_UUID)
        self.frankie_order = Order(self.frankie.customer_UUID, self.frankie_payment.payment_option_UUID)
        self.brass_knuckles = Product("Brass Knuckles", 19.99)
        self.frankie_order_line_item = OrderLineItem(self.frankie_order.order_UUID, self.brass_knuckles.product_UUID)

    def test_order_line_item_creation(self):
        self.assertEqual(self.frankie_order_line_item.order_UUID, self.frankie_order.order_UUID)
        self.assertEqual(self.frankie_order_line_item.product_UUID, self.brass_knuckles.product_UUID)

if __name__ == '__main__':
    unittest.main()

