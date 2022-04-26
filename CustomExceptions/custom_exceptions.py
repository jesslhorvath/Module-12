class InvalidCustomerIdException(Exception):
    def __init__(self, message="Customer ID is not in 1000-9999 range"):
        self.message = message
        super().__init__(self.message)

class InvalidNameException(Exception):
    def __init__(self, message="Name must contain all alpha characters"):
        self.message = message
        super().__init__(self.message)

class InvalidPhoneNumberFormat(Exception):
    def __init__(self, message="Phone number must be in the 000-000-0000 format"):
        self.message = message
        super().__init__(self.message)