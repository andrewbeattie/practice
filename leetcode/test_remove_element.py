import unittest
from remove_element import Solution

class TestSolution(unittest.TestCase):
    def test_upper_case(self):
        s = Solution()
        input = "Hello World"
        self.assertEqual(s.lengthOfLastWord(input), 5)

    def test_lower_case(self):
        s = Solution()
        input = "luffy is still joyboy"
        self.assertEqual(s.lengthOfLastWord(input), 6)
        
    def test_spaces_at_end(self):
        s = Solution()
        input = "   fly me   to   the moon  "
        self.assertEqual(s.lengthOfLastWord(input), 4)