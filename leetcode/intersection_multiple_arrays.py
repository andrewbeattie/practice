from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dupes = []
        flat = []
        for sublist in nums:
            for item in set(sublist):
                flat.append(item)
        for f in flat:
            if flat.count(f) >= len(nums):
                if f not in dupes:
                    dupes.append(f)
        dupes.sort()
        return dupes




                

        
        