import unittest
from products import *


class TestProducts(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.brass_knuckles = Product("Brass Knuckles", 19.99)

    def test_product_creation(self):
        self.assertIsNotNone(self.brass_knuckles.product_UUID)
        self.assertEqual("Brass Knuckles", self.brass_knuckles.name_of_product)
        self.assertEqual(19.99, self.brass_knuckles.unit_cost_of_product)


    def test_product_retrieval(self):
        self.products = Product.read_products()
        self.product_type_list = []

        for product in self.products:
            self.product_type_list.append(product["product_name"])
            self.product_type_list.append(product["product_price"])
        self.assertIn("Brass Knuckles", self.product_type_list)
        self.assertIn(19.99, self.product_type_list)

if __name__ == '__main__':
    unittest.main()
