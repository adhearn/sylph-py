import unittest

from . import Interpreter, DictEnvironment


class TestBasics(unittest.TestCase):
    def test_primitives_numbers(self):
        interp = Interpreter()
        self.assertEqual(interp.eval(7), 7)
        self.assertEqual(interp.eval(-42), -42)


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


class TestEnv(unittest.TestCase):
    def test_simple(self):
        env = DictEnvironment()
        env = env.extend("a", 23)
        self.assertEqual(env.lookup("a"), 23)


class TestLambda(unittest.TestCase):
    def test_simple(self):
        interp = Interpreter()
        expr = [["lambda", ["x"], "x"], 42]
        val = interp.eval(expr)
        self.assertEqual(val, 42)

    def test_add1(self):
        interp = Interpreter()
        expr = [["lambda", ["x"], ["+", "x", 1]], 42]
        val = interp.eval(expr)
        self.assertEqual(val, 43)

    def test_curried(self):
        interp = Interpreter()
        expr = [[["lambda", ["x"], ["lambda", ["y"], ["+", "x", "y"]]], 23], 42]
        val = interp.eval(expr)
        self.assertEqual(val, 65)


if __name__ == '__main__':
    unittest.main()
