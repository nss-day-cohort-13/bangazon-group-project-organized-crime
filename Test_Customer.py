import unittest

from customer import *

class Test_customer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.frankie = Customer("Frankie the Nose", "100 thief ave", "Bellvue", "TN", "37204", "615-867-5309")

    def test_customer_creation(self):
        self.assertEqual("Frankie the Nose", self.frankie.name)
        self.assertEqual("100 thief ave", self.frankie.address)
        self.assertEqual("Bellvue", self.frankie.city)
        self.assertEqual("TN", self.frankie.state)
        self.assertEqual("37204", self.frankie.zip)
        self.assertEqual("615-867-5309", self.frankie.phone)
        self.assertIsNotNone(self.frankie.customer_UUID)

    @staticmethod
    def test_customer_retrieval(self):
        customers = Customer.read_customers()
        customer_list = []
        for customer_name in customers:
            customer_list.append(customer_name["customer_name"])
        self.assertIn("Frankie the Nose", customer_list)
