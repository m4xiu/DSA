class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        bit = [0] * (2 * n + 3)

        def add(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        cur = n + 1
        add(cur)
        ans = 0

        for x in nums:
            cur += 1 if x == target else -1
            ans += query(cur - 1)
            add(cur)

        return ans