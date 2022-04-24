"""
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

"""
from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        # create a sorted copy of nums
        n_num=nums.copy()
        n_num.sort()
        # rotate through nums and check to see if it matches the sorted list
        for i in range(len(nums)):
            nums.append(nums[0])
            nums.pop(0)
            if nums==n_num:
                return True
        return False
