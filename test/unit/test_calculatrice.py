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

    def test_multiplication(self):
        a_data = [10,-53, 12, -45,-42, 0]
        b_data = [10,2,-17, -7, 0, 17]
        attendu_data = [100, -106, -204, 315, 0]

        for index in range(len(attendu_data)):
            a = a_data[index]
            b = b_data[index]
            attendu = attendu_data[index]
            with self.subTest(a=a, b=b, attendu=attendu):
                obtenu = self.calculatrice.multiplication(a, b)
                self.assertEqual(attendu, obtenu, "test case %d" % (index + 1))
    
    def test_division(self):
        a_data = [17,0,54,-12,20,-24]
        b_data = [2,2,0,6,-10,-12]
        attendu_data = [8,0,None, -2,-2,2]

        for index in range(len(attendu_data)):
            a = a_data[index]
            b = b_data[index]
            attendu = attendu_data[index]
            with self.subTest(a=a, b=b, attendu=attendu):
                obtenu = self.calculatrice.division(a, b)
                self.assertEqual(attendu, obtenu, "test case %d" % (index + 1))

    def test_matrice(self):
        a_data = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
        b_data = [[[12, 4],[43, 12],[1, 2]], [[3, 6], [12, 32]]]
        attendu_data = [[[12, 4],[43, 12],[1, 2]], None]

        for index in range(len(attendu_data)):
            a = a_data[index]
            b = b_data[index]
            attendu = attendu_data[index]
            with self.subTest(a=a, b=b, attendu=attendu):
                obtenu = self.calculatrice.produitMatrice(a, b)
                self.assertEqual(attendu, obtenu, "test case %d" % (index + 1))

if __name__ == '__main__':
    unittest.main()