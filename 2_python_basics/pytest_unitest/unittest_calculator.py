import unittest
import calculator

class TestCalculator(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(calculator.suma(3, 5), 8)
        
    def test_resta(self):
        self.assertEqual(calculator.resta(5, 3), 2)
        
    def test_multiplicacion(self):
        self.assertEqual(calculator.multiplicacion(3, 5), 15)
        

if __name__== "__main__":
    unittest.main()
    