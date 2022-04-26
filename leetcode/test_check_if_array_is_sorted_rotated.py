import unittest
from check_if_array_is_sorted_rotated import Solution

class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        nums = [3,4,5,1,2]
        self.assertEqual(s.check(nums), True)

    def test_two(self):
        s = Solution()
        nums = [2,1,3,4]
        self.assertEqual(s.check(nums), False)

    def test_three(self):
        s = Solution()
        nums = [1,2,3]
        self.assertEqual(s.check(nums), True)
