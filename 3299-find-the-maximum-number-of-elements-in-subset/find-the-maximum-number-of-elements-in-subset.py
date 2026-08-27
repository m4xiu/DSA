from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        ans = cnt[1] if cnt[1] % 2 else max(1, cnt[1] - 1)

        for x in cnt:
            if x == 1:
                continue

            y = x
            length = 1

            while cnt[y] >= 2:
                y *= y
                length += 2

                if y > 10**9:
                    break

            if cnt[y] == 0:
                length -= 2

            ans = max(ans, length)

        return ans