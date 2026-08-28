class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if n == 1:
            return 0

        # Column prefix sums
        pre = [[0] * (n + 1) for _ in range(n)]

        for c in range(n):
            for r in range(n):
                pre[c][r + 1] = pre[c][r] + grid[r][c]

        # dpPick[x]  = best score when current column is selected
        # dpSkip[x]  = best score when current column is not selected
        dpPick = [0] * (n + 1)
        dpSkip = [0] * (n + 1)

        for c in range(1, n):
            newPick = [0] * (n + 1)
            newSkip = [0] * (n + 1)

            for cur in range(n + 1):
                for prev in range(n + 1):

                    if cur > prev:
                        # Gain comes from column c-1
                        gain = pre[c - 1][cur] - pre[c - 1][prev]

                        newPick[cur] = max(
                            newPick[cur],
                            dpSkip[prev] + gain
                        )

                        newSkip[cur] = max(
                            newSkip[cur],
                            dpSkip[prev] + gain
                        )

                    else:
                        # Gain comes from column c
                        gain = pre[c][prev] - pre[c][cur]

                        newPick[cur] = max(
                            newPick[cur],
                            dpPick[prev] + gain
                        )

                        newSkip[cur] = max(
                            newSkip[cur],
                            dpPick[prev]
                        )

            dpPick = newPick
            dpSkip = newSkip

        return max(dpPick)