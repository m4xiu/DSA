class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        p = nums [0]

        for i in range(1,n):
            if nums[i] == nums[i -1] + 1:p += nums [i]
            else: break

        s = set(nums)
        while True:
            if not p in s: return p
            p += 1