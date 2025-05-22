import unittest
from refactored02 import process_order

class TestOrderProcessing(unittest.TestCase):

    def test_valid_credit_card_order(self):
        order = {
            "payment_type": "credit_card",
            "card_number": "123456781234568",
            "expiration_date": "12/24",
            "card_security_code": "123",
            "shipping_address": "123 Main St",
            "quantity": 2,
            "price": 100.0
        }
        try:
            process_order(order)
        except Exception:
            self.fail("process_order() raised an exception on valid input")


    def test_invalid_card_number(self):
        order = {
            "payment_type": "credit_card",
            "card_number": "1234",  # Wrong length di ha
            "expiration_date": "12/24",
            "card_security_code": "123",
            "shipping_address": "123 Main St",
            "quantity": 2,
            "price": 100.0
        }
        with self.assertRaises(ValueError):
            process_order(order)

    def test_missing_shipping_address(self):
        order = {
            "payment_type": "paypal",
            "paypal_email": "user@example.com",
            "quantity": 1,
            "price": 50.0
        }
        with self.assertRaises(ValueError):
            process_order(order)

    def test_zero_quantity(self):
        order = {
            "payment_type": "paypal",
            "paypal_email": "user@example.com",
            "shipping_address": "123 Main St",
            "quantity": 0,
            "price": 100.0
        }
        with self.assertRaises(ValueError):
            process_order(order)

    def test_invalid_payment_type(self):
        order = {
            "payment_type": "bitcoin",  # Not supported
            "shipping_address": "123 Main St",
            "quantity": 1,
            "price": 100.0
        }
        with self.assertRaises(ValueError):
            process_order(order)

    def test_assertion_error_for_invalid_payment_type(self):
        order = {
            "payment_type": "bitcoin",  # Invalid payment type to trigger assertion
            "card_number": "1234567812345678",
            "expiration_date": "12/24",
            "card_security_code": "123",
            "shipping_address": "123 Main St",
            "quantity": 2,
            "price": 100.0
        }

        with self.assertRaises(ValueError):  # Error aaye 'bitcoin' valid nahi ha
            process_order(order)


if __name__ == '__main__':
    unittest.main()
