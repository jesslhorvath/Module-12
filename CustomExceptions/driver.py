from custom_exceptions import InvalidCustomerIdException, InvalidNameException, InvalidPhoneNumberFormat
from customer import Customer as c

try:
    customerA = c("5000", "Jona4", "Joe", "123-456-7890")
except Exception as e:
    print(e)

try:
    customerB = c("2", "Jonas", "Joe", "123-456-7890")
except Exception as e:
    print(e)

try:
    customerC = c("5000", "Jonas", "Joe", "one-two-three-four-five-six-seven-eight-nine-zero")
except Exception as e:
    print(e)
