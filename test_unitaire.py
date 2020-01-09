from calculatrice import *
import unittest

class Test_calculatrice(unittest.TestCase):

    def test_addition(self):

        calculatrice = Calculatrice()
            
        res_addition = calculatrice.addition(2,3)

        self.assertEqual(res_addition,5)


    def test_soustraction(self):

        calculatrice = Calculatrice()
        
        res_soustraction = calculatrice.soustraction(5,3)
        
        self.assertEqual(res_soustraction,2)


    def test_multiplication(self):
        
        calculatrice = Calculatrice()
        
        res_multiplication = calculatrice.multiplication(2,5)
        
        self.assertEqual(res_multiplication,10)
        
        res_multiplication2 = calculatrice.multiplication(5,2)
        
        self.assertEqual(res_multiplication,res_multiplication2)


    def test_division(self):

        calculatrice = Calculatrice()
        
        res_division = calculatrice.division(5,2)
        
        self.assertEqual(res_division,2.5)
        
        self.assertRaises(Exception, calculatrice.division,5,0)
        
    def test_puissance(self):
        
        calculatrice = Calculatrice()
        
        res_puissance = calculatrice.puissance(2,3)
        
        self.assertEqual(res_puissance, 8)


if __name__ == '__main__':
    unittest.main()