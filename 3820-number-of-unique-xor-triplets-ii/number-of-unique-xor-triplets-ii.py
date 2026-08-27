class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s = set(nums)
        ans = set()

        for x in s:
            for y in s:
                ans.add(x ^ y)

        result = set()

        for x in ans:
            for y in s:
                result.add(x ^ y)

        return len(result)