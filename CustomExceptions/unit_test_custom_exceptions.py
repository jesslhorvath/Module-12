import unittest
from customer import Customer as c


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.customer = c("4000", "Jo", "Jim", "515-555-1234")

    def tearDown(self):
        del self.customer

    def test_object_created_required_attributes(self):
        self.assertEqual(self.customer.last_name, "Jo")
        self.assertEqual(self.customer.first_name, "Jim")
        self.assertEqual(self.customer.customer_id, "4000")
        self.assertEqual(self.customer.phone_number, "515-555-1234")

    def test_object_created_all_attributes(self):
        customer = c("4000", "Jo", "Jim", "515-555-1234")
        assert customer.last_name == "Jo"
        assert customer.first_name == "Jim"
        assert customer.customer_id == "4000"
        assert customer.phone_number == "515-555-1234"

    def test_student_str(self):
        assert self.customer.__str__()

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            cus = c("4000", "Jo3", "Jim", "515-555-1234")

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            cus = c("4000", "Jo", "J1m", "515-555-1234")

    def test_object_not_created_error_phone(self):
        with self.assertRaises(ValueError):
            cus = c("4000", "Jo", "Jim", "515555one234")
    
    def test_object_not_created_error_cid(self):
        with self.assertRaises(ValueError):
            cus = c("1", "Jo", "Jim", "515-555-1234")

if __name__ == '__main__':
    unittest.main()