from sortedcontainers import SortedList

class BIT:
    def __init__(self, n):
        self.a = [0] * (n + 1)

    def update(self, i, v):
        i += 1
        while i < len(self.a):
            self.a[i] = max(self.a[i], v)
            i += i & -i

    def query(self, i):
        i += 1
        ans = 0
        while i:
            ans = max(ans, self.a[i])
            i -= i & -i
        return ans

class Solution:
    def getResults(self, queries):
        n = min(50000, len(queries) * 3)

        obs = SortedList([0, n])

        for q in queries:
            if q[0] == 1:
                obs.add(q[1])

        bit = BIT(n + 1)

        for i in range(1, len(obs)):
            bit.update(obs[i], obs[i] - obs[i - 1])

        ans = []

        for q in reversed(queries):
            x = q[1]

            if q[0] == 1:
                i = obs.bisect_left(x)
                prev = obs[i - 1]
                nxt = obs[i + 1]

                obs.pop(i)

                bit.update(nxt, nxt - prev)

            else:
                sz = q[2]
                i = obs.bisect_right(x)
                prev = obs[i - 1]

                ans.append(bit.query(prev) >= sz or x - prev >= sz)

        return ans[::-1]