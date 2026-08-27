class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        a = restrictions + [[1, 0]]
        a.sort()

        if a[-1][0] != n:
            a.append([n, n - 1])

        for i in range(1, len(a)):
            a[i][1] = min(a[i][1], a[i-1][1] + a[i][0] - a[i-1][0])

        for i in range(len(a)-2, -1, -1):
            a[i][1] = min(a[i][1], a[i+1][1] + a[i+1][0] - a[i][0])

        ans = 0

        for i in range(1, len(a)):
            d = a[i][0] - a[i-1][0]
            h = (a[i][1] + a[i-1][1] + d) // 2
            ans = max(ans, h)

        return ans