class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            ans = float('-inf')

            ans = max(ans, stoneValue[i] - dp[i + 1])

            if i + 1 < n:
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] - dp[i + 2])

            if i + 2 < n:
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3])

            dp[i] = ans
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
            