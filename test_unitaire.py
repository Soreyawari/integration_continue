from calculatrice import *
import unittest

class Test_calculatrice(unittest.TestCase):

	def test_addition(self):
		lexical = Lexical("main.c")
		calculatrice = Calculatrice()

		res_addition = calculatrice.addtion(2,3)

		self.assertEqual(res_addition,5)

	def test_soustraction(self):
		pass

	def test_multiplication(self):
		pass

	def test_division(self):
		pass



if __name__ == '__main__':
    unittest.main()