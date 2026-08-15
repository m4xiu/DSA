class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if all(x == 0 for x in nums):
            return 0
        total_xor = functools.reduce(lambda x, y: x ^ y, nums, 0)
        if total_xor != 0:
            return n
        else:
            return n - 1
