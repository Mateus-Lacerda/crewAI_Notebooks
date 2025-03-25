import unittest

def divide(a, b):
    """Function to divide two numbers."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

class TestDivideFunction(unittest.TestCase):

    def test_basic_division_positive_integers(self):
        """Test basic division of positive integers"""
        self.assertEqual(divide(10, 2), 5.0)

    def test_division_negative_integer_by_positive(self):
        """Test division of a negative integer by a positive integer"""
        self.assertEqual(divide(-10, 2), -5.0)

    def test_division_positive_integer_by_negative(self):
        """Test division of a positive integer by a negative integer"""
        self.assertEqual(divide(10, -2), -5.0)

    def test_division_two_negative_integers(self):
        """Test division of two negative integers"""
        self.assertEqual(divide(-10, -2), 5.0)

    def test_division_resulting_in_float(self):
        """Test division resulting in a float"""
        self.assertEqual(divide(5, 2), 2.5)

    def test_division_by_zero(self):
        """Test division by zero raises ZeroDivisionError"""
        with self.assertRaises(ZeroDivisionError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "division by zero")

    def test_division_float_numbers(self):
        """Test division of float numbers"""
        self.assertAlmostEqual(divide(10.5, 2.5), 4.2, places=1)

    def test_division_recurring_decimal(self):
        """Test division where the result is a recurring decimal"""
        self.assertAlmostEqual(divide(1, 3), 0.3333, places=4)

    def test_division_float_by_integer(self):
        """Test division of a float by an integer"""
        self.assertEqual(divide(5.0, 2), 2.5)

    def test_division_zero_by_non_zero_integer(self):
        """Test division of zero by a non-zero integer"""
        self.assertEqual(divide(0, 5), 0.0)

if __name__ == '__main__':
    unittest.main()