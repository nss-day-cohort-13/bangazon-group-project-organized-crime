import unittest

from products import *


class TestProducts(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.brass_knuckles = Product("Brass Knuckles", 19.99)

    def test_product_creation(self):
        self.assertEqual("Brass Knuckles", self.brass_knuckles.product_name)
        self.assertEqual(19.99, self.brass_knuckles.product_price)
        self.assertIsNotNone(self.brass_knuckles.product_UUID)

    @staticmethod
    def test_product_retrieval(self):
        products = Product.read_products()
        product_type_list = []

        for product_name in products:
            product_type_list.append(product_name["product_name"])
            product_type_list.append(product_name["product_price"])
        self.assertIn("Brass Knuckles", product_type_list)
        self.assertIn(19.99, product_type_list)

if __name__ == '__main__':
    unittest.main()
