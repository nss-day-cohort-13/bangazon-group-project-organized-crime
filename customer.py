import sqlite3

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
                 customer_phone
                 ):

        self.customer_UUID = None
        self.name = customer_name
        self.address = customer_address
        self.city = customer_city
        self.state = customer_state
        self.zipcode = customer_zip
        self.phone = customer_phone
        self.customer_object = {
                                "customer_UUID": self.customer_UUID,
                                "name": self.name,
                                "address": self.address,
                                "city": self.city,
                                "state": self.state,
                                "zipcode": self.zipcode,
                                "phone": self.phone
                                }
        self.write_to_customer()

    def write_to_customer(self):

        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

            c.execute   ("insert into customer values(?,?,?,?,?,?,?)",
                            (
                            self.customer_UUID,
                            self.name,
                            self.address,
                            self.city,
                            self.state,
                            self.zipcode,
                            self.phone
                            )
                        )
            conn.commit()


    def read_customers():
        customer_list = []
        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

        for row in c.execute("""SELECT * FROM Customer c"""):
            customer_list.append(row)
        print(customer_list[1][0])




if __name__ == '__main__':
    Customer.read_customers()
    # Customer("Bob Cocker", "456 Your Street", "Memphis", "TN", "99999", "(123) 456-7890")
