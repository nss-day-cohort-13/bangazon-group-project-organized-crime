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
