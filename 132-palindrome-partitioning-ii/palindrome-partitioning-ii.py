class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        pal = [[False] * n for _ in range(n)]
        dp = list(range(n))

        for r in range(n):
            for l in range(r + 1):
                if s[l] == s[r] and (r - l <= 2 or pal[l + 1][r - 1]):
                    pal[l][r] = True

                    if l == 0:
                        dp[r] = 0
                    else:
                        dp[r] = min(dp[r], dp[l - 1] + 1)

        return dp[-1]    