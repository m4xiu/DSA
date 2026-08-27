class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == target:
                    cnt += 1

                if cnt * 2 > j - i + 1:
                    ans += 1

        return ans