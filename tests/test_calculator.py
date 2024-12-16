# unitTest is part of standard library.
# subclass with unittest.TestCase
# each test case cvan have 1 or morte test methods.
# will recognise tests starting with test_
# Assertion methods: assertequal, assertTrue assertFalse
# validate output is expected value.
# python3 -m unittest file_name

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def test_calculator_class_exists(self):
        calc = Calculator() # make an instance of the calc class. 
        self.assertIsInstance(calc, Calculator) # test if calc is instance of calculator. 

    def test_add_method_exists(self):
        calc = Calculator()
        self.assertTrue(callable(getattr(calc, "add", None)))

    def test_add_method_has_two_inputs(self):
        calc = Calculator()
        self.assertEqual(calc.add(0,0), 0)

    def test_add_method_input_validation(self):
        calc = Calculator()
        with self.assertRaisesRegex(TypeError, "Custom Error: input should be numeric"):
            calc.add("a", 5)

    def test_add_method_performs_addition(self):
        calc = Calculator()
        self.assertEqual(calc.add(3, 2), 5)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(300, 200), 500)