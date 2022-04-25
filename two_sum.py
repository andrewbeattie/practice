from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target - num], i]
            else:
                num_map[num] = i
        return []
        # for i in range(len(nums)):
        #     val = target - nums[i]
        #     if val in nums:
        #         if i != nums.index(val):
        #             sums = [i, nums.index(val)]
        #             sums.sort()
        #             return sums
        # return []
        # for i, n in enumerate(nums):
        #     initial = target - n
        #     if initial in nums:
        #         if i != nums.index(initial):
        #             sums = [i, nums.index(initial)]
        #             sums.sort()
        #             return sums
        # return []
