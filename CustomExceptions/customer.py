from custom_exceptions import InvalidCustomerIdException, InvalidNameException, InvalidPhoneNumberFormat
import re

class Customer:
    """Customer class"""

    def __init__(self, cid, lname, fname, pnumber):  # Constructor sets all to no value
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_number_characters = set("1234567890-()")
        customer_id_characters = set("1234567890")
        phone_regex = re.compile(r"\d{3}-\d{3}-\d{4}")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise InvalidNameException
        if not phone_number_characters.issuperset(pnumber):
            raise InvalidPhoneNumberFormat
        if not phone_regex.match(pnumber):
            raise InvalidPhoneNumberFormat
        if not customer_id_characters.issuperset(cid):
            raise InvalidCustomerIdException
        elif not int(cid) in range(1000,10000):
            raise InvalidCustomerIdException
        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnumber

    def __str__(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number

    def __repr__(self):
        return 'Customer({},{},{},{})'.format(self.customer_id, self.last_name, self.first_name, self.phone_number)

    def change_last_name(self, name):
        self.last_name = name

    def change_first_name(self, name):
        self.first_name = name

    def change_phone_number(self, number):
        self.phone_number = number

    def display(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number
