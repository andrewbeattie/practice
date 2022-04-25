import unittest
from two_sum import Solution

class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        nums = [2,7,11,15]
        target = 9
        self.assertEqual(s.twoSum(nums, target), [0, 1])

    def test_two(self):
        s = Solution()
        nums = [3,2,4]
        target = 6
        self.assertEqual(s.twoSum(nums, target), [1,2])

    def test_three(self):
        s = Solution()
        nums = [3,3]
        target = 6
        self.assertEqual(s.twoSum(nums, target), [0,1])

        