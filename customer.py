from utility import *
import uuid


class Customer:
    '''
    allows creation of an instance of a customer class

    keyword arguments:
    customer_name: saved as a variable. a component of the customer object.

    customer_address: saved as a variable. a component of the customer object.

    customer_city: saved as a variable. a component of the customer object.

    customer_state: saved as a variable. a component of the customer object.

    customer_zip: saved as a variable. a component of the customer object.

    customer_phone: saved as a variable. a component of the customer object.
    '''

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
        self.write_to_database()

if __name__ == '__main__':
    Customer.read_customers()
