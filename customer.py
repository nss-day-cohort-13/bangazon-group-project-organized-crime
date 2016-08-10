import pickle
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
        self.serialize_customer()
        # self.read_customers()

    def serialize_customer(self):
        '''
        using pickle, serializes the customer_object, writing it to a
        text file.
        '''
        # self.customer_dict = {}
        # self.customer_dict.update(user_object)
        with open('customers.txt', 'ab+') as f:
            pickle.dump(self.customer_object, f)

    @staticmethod
    def read_customers():
        '''
        using pickle, deserializes customer_objects from txt file
        and adds each item to a list, which is then returned, allowing access
        to customer data in other modules
        '''
        customer_list = []
        with open('customers.txt', 'rb+') as f:
            while True:
                try:
                    customer_list.append(pickle.load(f))
                except EOFError:
                    break
            print(customer_list)
            return customer_list

if __name__ == '__main__':
    Customer.read_customers()
