import unittest
from create_phone_number import create_phone_number_1

class TestCreatePhoneNumber(unittest.TestCase):
    def test_create_phone_number(self):
        assert create_phone_number_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
        assert create_phone_number_1([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"
