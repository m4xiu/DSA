class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        a = sorted((x, i) for i, x in enumerate(nums))
        pos = [0] * n
        val = [0] * n

        for i, (x, idx) in enumerate(a):
            val[i] = x
            pos[idx] = i

        right = [0] * n
        j = 0

        for i in range(n):
            j = max(j, i)
            while j + 1 < n and val[j + 1] - val[i] <= maxDiff:
                j += 1
            right[i] = j

        LOG = n.bit_length()
        up = [right]

        for k in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            u = pos[u]
            v = pos[v]

            if u > v:
                u, v = v, u

            if u == v:
                ans.append(0)
                continue

            if right[u] >= v:
                ans.append(1)
                continue

            if right[u] == u:
                ans.append(-1)
                continue

            steps = 0

            for k in range(LOG - 1, -1, -1):
                x = up[k][u]
                if x < v:
                    u = x
                    steps += 1 << k

            if right[u] >= v:
                ans.append(steps + 1)
            else:
                ans.append(-1)

        return ans
        