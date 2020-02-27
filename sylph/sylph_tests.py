import unittest

from . import Interpreter


class TestBasics(unittest.TestCase):
    def test_primitives_numbers(self):
        interp = Interpreter()
        self.assertEqual(interp.eval(7), 7)
        self.assertEqual(interp.eval(-42), -42)

    def test_primitives_strings(self):
        interp = Interpreter()
        self.assertEqual(interp.eval("Test String"), "Test String")
        self.assertEqual(interp.eval('Single quote test string'), 'Single quote test string')

class TestArithmetic(unittest.TestCase):
    def test_addition(self):
        interp = Interpreter()
        simple = ["+", 23, 42]
        self.assertEqual(interp.eval(simple), 65)

        complex = ["+", ["+", 2, 3], ["+", 23, 42]]
        self.assertEqual(interp.eval(complex), 70)

    def test_subtraction(self):
        interp = Interpreter()
        simple = ["-", 23, 42]
        self.assertEqual(interp.eval(simple), -19)

        complex = ["-", ["-", 42, 23], ["-", 3, 2]]
        self.assertEqual(interp.eval(complex), 18)

    def test_multiplication(self):
        interp = Interpreter()
        simple = ["*", 2, 3]
        self.assertEqual(interp.eval(simple), 6)

    def test_various(self):
        interp = Interpreter()
        expr = ["*", ["+", 4, 5], ["-", 8, 5]]
        self.assertEqual(interp.eval(expr), 27)


if __name__ == '__main__':
    unittest.main()
