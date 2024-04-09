import unittest
from list_filter import filter_list

class TestListFilter(unittest.TestCase):
    def test_create_phone_number(self):
        assert filter_list([1, 2, "a"]) == [1, 2]
        assert filter_list(["a", 2, 3]) == [2, 3]
