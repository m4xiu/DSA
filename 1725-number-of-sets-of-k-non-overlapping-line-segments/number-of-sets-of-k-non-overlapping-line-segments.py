class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        end = [[0] * (k + 1) for _ in range(n + 1)]

        dp[1][0] = 1

        for i in range(2, n + 1):
            for j in range(k + 1):
                dp[i][j] = (dp[i-1][j] + end[i-1][j]) % MOD
                end[i][j] = end[i-1][j]

                if j:
                    end[i][j] += dp[i-1][j-1]
                    end[i][j] += end[i-1][j-1]
                    end[i][j] %= MOD

        return (dp[n][k] + end[n][k]) % MOD