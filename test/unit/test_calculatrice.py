import unittest

from src.packageCalc.calculatrice import Calculatrice

class TestCalculatrice(unittest.TestCase):
    def setUp(self):
        self.calculatrice = Calculatrice()

    def test_addition(self):
        a_data = [4, -2,5,-2,10,0,-20,0]
        b_data = [6,12,-2,-2,0,70,0,-70]
        attendu_data = [10,10,3,-4,10,70,-20,-70]

        for index in range(len(attendu_data)):
            a = a_data[index]
            b = b_data[index]
            attendu = attendu_data[index]
            with self.subTest(a=a, b=b, attendu=attendu):
                obtenu = self.calculatrice.addition(a, b)
                self.assertEqual(attendu, obtenu, "test case %d" % (index+1))
    
    def test_soustraction(self):
        a_data = [2,-1, 2,-5,5,0,-5, 0, 0, 5, -5]
        b_data = [3,2,-1, -1, 0,5,0,-5, 0, 4, -6]
        attendu_data = [-1,-3, 3,-4,5,-5,-5,5,0, 1,1]

        for index in range(len(attendu_data)):
            a = a_data[index]
            b = b_data[index]
            attendu = attendu_data[index]
            with self.subTest(a=a, b=b, attendu=attendu):
                obtenu = self.calculatrice.soustraction(a, b)
                self.assertEqual(attendu, obtenu, "test case %d" % (index + 1))

if __name__ == '__main__':
    unittest.main()