#!/usr/bin/python3
"""Is Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ The Class for tests
    """

    def test_positive_list(self):
        """ Tests the function on a list of positives """
        self.assertEqual(max_integer([10, 5, 90, 45, 35]), 90)

    def test_negative_list(self):
        """ Tests the function on a list of negatives """
        self.assertEqual(max_integer([-22, -17, -15, -13, -6]), -6)

    def test_error(self):
        """ Tests the function on a error case """
        with self.assertRaises(TypeError):
            max_integer(['n', 8, 10])

    def test_none(self):
        """ Tests the function with None parameter """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_empty_list(self):
        """ Tests the function on a empty list case """
        self.assertEqual(max_integer([]), None)

    def test_unique_int(self):
        """ Tests the function on a list with a single value """
        self.assertEqual(max_integer([51]), 51)

    def test_ordered_list(self):
        """ Tests the function on a ordered list """
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)

    def test_reversed_list(self):
        """ Tests the function on a reversed ordered list """
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_positives_and_negatives(self):
        """ Test the function on a list with positive and negative values """
        self.assertEqual(max_integer([-3, 2, 5, -99]), 5)


if __name__ == "__main__":
    unittest.main()
