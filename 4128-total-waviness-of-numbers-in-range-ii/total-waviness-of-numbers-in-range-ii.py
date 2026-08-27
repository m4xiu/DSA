from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n):
            if n < 100:
                return 0

            d = list(map(int, str(n)))

            @lru_cache(None)
            def dp(i, a, b, started, tight):
                if i == len(d):
                    return (1, 0)

                limit = d[i] if tight else 9
                cnt = total = 0

                for x in range(limit + 1):
                    nt = tight and x == limit

                    if not started and x == 0:
                        c, s = dp(i + 1, 10, 10, 0, nt)
                        cnt += c
                        total += s
                    else:
                        add = 0
                        if started and a != 10:
                            if (b > a and b > x) or (b < a and b < x):
                                add = 1

                        c, s = dp(i + 1, b, x, 1, nt)
                        cnt += c
                        total += s + add * c

                return cnt, total

            return dp(0, 10, 10, 0, True)[1]

        return solve(num2) - solve(num1 - 1) 