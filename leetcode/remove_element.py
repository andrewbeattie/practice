class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #interesting .lstrip().rstrip() is faster compared to strip()
        return len(s.lstrip().rstrip().split(" ")[-1])
        