import unittest
from running_sum_1d import Solution

class TestSolution:
    def test_running_sum(self):
        s = Solution()
        self.assertEqual(s.runningSum([1,2,3,4]), [1,3,6,10])

    
    def test_running_sum_fail(self):
        s = Solution()
        self.assassertNotEqual(s.runningSum([1, 2, 3, 4]), [1, 3, 6, 10])
