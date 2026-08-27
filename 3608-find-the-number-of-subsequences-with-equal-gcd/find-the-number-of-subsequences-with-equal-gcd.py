from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        m = max(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [[0] * (m + 1) for _ in range(m + 1)]

            for a in range(m + 1):
                for b in range(m + 1):
                    if dp[a][b] == 0:
                        continue

                    v = dp[a][b]

                    ndp[a][b] = (ndp[a][b] + v) % MOD
                    ndp[gcd(a, x)][b] = (ndp[gcd(a, x)][b] + v) % MOD
                    ndp[a][gcd(b, x)] = (ndp[a][gcd(b, x)] + v) % MOD

            dp = ndp

        ans = 0

        for g in range(1, m + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans