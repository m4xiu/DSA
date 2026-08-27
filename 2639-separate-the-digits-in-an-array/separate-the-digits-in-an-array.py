class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(c) for x in nums for c in str(x)]