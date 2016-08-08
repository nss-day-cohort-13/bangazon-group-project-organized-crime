import pickle
import uuid


class Customer:

    def __init__(self,
                 customer_name,
                 customer_address,
                 customer_city,
                 customer_state,
                 customer_zip,
                 customer_phone):

        self.name = customer_name
        self.address = customer_address
        self.city = customer_city
        self.state = customer_state
        self.zipcode = customer_zip
        self.phone = customer_phone
        self.customer_UUID = uuid.uuid4().int
        self.customer_object = {"name": self.name,
                                "address": self.address,
                                "city": self.city,
                                "state": self.state,
                                "zipcode": self.zipcode,
                                "phone": self.phone,
                                "customer_UUID": self.customer_UUID}
        self.serialize_customer()
        # self.read_customers()

    def serialize_customer(self):
        # self.customer_dict = {}
        # self.customer_dict.update(user_object)
        with open('customers.txt', 'ab+') as f:
            pickle.dump(self.customer_object, f)

    def read_customers(self):
        self.customer_list = []
        with open('customers.txt', 'rb+') as f:
            while True:
                try:
                    self.customer_list.append(pickle.load(f))
                except EOFError:
                    break
            print(self.customer_list)
            return self.customer_list
