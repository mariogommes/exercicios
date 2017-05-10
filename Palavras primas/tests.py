import unittest
import prime_word

class Prime_Word_Tests(unittest.TestCase):
	
	def test_isPrime_Works_With_Prime(self):
		prime_number = 2
		result = prime_word.isPrime(prime_number)
		self.assertTrue(result)

	def test_isPrime_Works_With_No_Prime(self):
		no_prime_number = 4
		result = prime_word.isPrime(no_prime_number)
		self.assertFalse(result)		

	def test_contWordNumbers_abc(self):
		abc_count = 6
		result = prime_word.countWordNumbers("abc")
		self.assertEqual(abc_count, result)

if __name__ == '__main__':
    unittest.main()