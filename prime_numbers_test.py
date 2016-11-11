import unittest
import prime_numbers

class PrimeNumbersTestCase(unittest.TestCase):
	#Test for function to take only integers as inputs
	def test_value_is_true(self):
		self.assertEqual(prime_numbers.append_prime_numbers(True), "Operation cannot allow " + str(type(True))+ ", integers only.")
	def test_value_is_true2(self):
		self.assertEqual(prime_numbers.append_prime_numbers(False), "Operation cannot allow " + str(type(False)) + ", integers only.")	
	def test_value_is_string(self):
		self.assertEqual(prime_numbers.append_prime_numbers("string"), "Operation cannot allow " + str(type("")) + ", integers only.")
	#Test for function to take only positive integers
	def test_numbers_less_than_one1(self):
		self.assertEqual(prime_numbers.append_prime_numbers(-20), "Prime numbers exist only for positive integers")
	def test_numbers_less_than_one2(self):
		self.assertEqual(prime_numbers.append_prime_numbers(-100), "Prime numbers exist only for positive integers")
	def test_numbers_less_than_one3(self):
		self.assertEqual(prime_numbers.append_prime_numbers(-150), "Prime numbers exist only for positive integers")
	def test_numbers_less_than_one4(self):
		self.assertEqual(prime_numbers.append_prime_numbers(-200), "Prime numbers exist only for positive integers")
	def test_numbers_less_than_one5(self):
		self.assertEqual(prime_numbers.append_prime_numbers(-1000), "Prime numbers exist only for positive integers")
	def test_value_is_dictionary(self):
		self.assertEqual(prime_numbers.append_prime_numbers({}), "Operation cannot allow " + str(type({})) + ", integers only.")
	def test_value_is_list(self):
		self.assertEqual(prime_numbers.append_prime_numbers([]), "Operation cannot allow " + str(type([])) + ", integers only.")



