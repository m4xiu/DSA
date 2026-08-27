class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [0] * n
        pre[0] = nums[0]

        for i in range(1, n):
            pre[i] = max(pre[i - 1], nums[i])

        ans = [0] * n
        suf = float('inf')

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                ans[i] = pre[i]
            elif pre[i] > suf:
                ans[i] = ans[i + 1]
            else:
                ans[i] = pre[i]

            suf = min(suf, nums[i])

        return ans
        
        