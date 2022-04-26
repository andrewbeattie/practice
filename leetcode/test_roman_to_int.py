import unittest
from roman_to_int import Solution

class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        string = "III"
        self.assertEqual(s.romanToInt(string), 3)

    def test_two(self):
        s = Solution()
        string = "LVIII"
        self.assertEqual(s.romanToInt(string), 58)

    def test_three(self):
        s = Solution()
        string = "MCMXCIV"
        self.assertEqual(s.romanToInt(string), 1994)

        