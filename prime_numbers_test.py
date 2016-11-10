import unittest
import prime_numbers

class PrimeNumbersTestCase(unittest.TestCase):
	def test_value_is_integer(self):
		self.assertEqual(prime_numbers.append_prime_numbers("string"), "Operation allows only integers!")



