import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set-up the Simplecalculator instance before each test"""
        self.calc = SimpleCalculator()
        
    def test_addition(self):
        """Test the addition method"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 7), 7)
        self.assertEqual(self.calc.add(-6, -6), -12)
        
    def test_subtraction(self):
        "Test the subtraction method"""
        self.assertEqual(self.calc.subtract(4, 5), -1)
        self.assertEqual(self.calc.subtract(5, 4), 1)
        self.assertEqual(self.calc.subtract(-6, -2), -4)
        self.assertEqual(self.calc.subtract(-9, 7), -16)
        self.assertEqual(self.calc.subtract(8, -4), 12)
        
    def test_multiplication(self):
        """Test the multiplication method"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-5, 7), -35)
        self.assertEqual(self.calc.multiply(-8, -9), 72)
        self.assertEqual(self.calc.multiply(0, 8), 0)
        
    def test_division(self):
        #Test the division method
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(5, 0), None)
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(5, 7), 5/7)
        self.assertEqual(self.calc.divide(-3, 4), -3/4)
        self.assertEqual(self.calc.divide(-6, -5), 6/5)
        self.assertEqual(self.calc.divide(8, -2), -4)