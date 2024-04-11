import unittest
from binary_addition import add_binary_1, add_binary_2, add_binary_3


class TestAddBinary1(unittest.TestCase):
    def test_add_binary(self):
        self.assertEqual(add_binary_1(1, 2), "11")
        self.assertEqual(add_binary_1(0, 0), "0")
        self.assertEqual(add_binary_1(1, 0), "1")
        self.assertEqual(add_binary_1(0, 1), "1")
        self.assertEqual(add_binary_1(2, 2), "100")
        self.assertEqual(add_binary_1(51, 12), "111111")

class TestAddBinary2(unittest.TestCase):
    def test_add_binary(self):
        self.assertEqual(add_binary_2(1, 2), "11")
        self.assertEqual(add_binary_2(0, 0), "0")
        self.assertEqual(add_binary_2(1, 0), "1")
        self.assertEqual(add_binary_2(0, 1), "1")
        self.assertEqual(add_binary_2(2, 2), "100")
        self.assertEqual(add_binary_2(51, 12), "111111")

class TestAddBinary3(unittest.TestCase):
    def test_add_binary(self):
        self.assertEqual(add_binary_3(1, 2), "11")
        self.assertEqual(add_binary_3(0, 0), "0")
        self.assertEqual(add_binary_3(1, 0), "1")
        self.assertEqual(add_binary_3(0, 1), "1")
        self.assertEqual(add_binary_3(2, 2), "100")
        self.assertEqual(add_binary_3(51, 12), "111111")