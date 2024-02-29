import unittest
from intersection_multiple_arrays import Solution

class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
        self.assertEqual(s.intersection(nums), [3,4])

    def test_two(self):
        s = Solution()
        nums = [[1,2,3],[4,5,6]]
        self.assertEqual(s.intersection(nums), [])

    def test_three(self):
        s = Solution()
        nums = [[7,34,45,10,12,27,13],[27,21,45,10,12,13]]
        self.assertEqual(s.intersection(nums), [10,12,13,27,45])

        