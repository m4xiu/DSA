class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i] = suffix[i + 1] + piles[i]

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, M):
            if i >= n:
                return 0 

            if 2 * M >= n - i:
                return suffix[i]

            best = 0

            for x in range(1, 2 * M + 1):
                best = max(best, suffix[i] - dp(i + x, max(M, x)))

            return best 

        return dp(0, 1)                  
        