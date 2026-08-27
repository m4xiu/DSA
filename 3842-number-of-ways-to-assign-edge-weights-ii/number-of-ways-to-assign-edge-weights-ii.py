class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 1000000007
        n = len(edges) + 1
        LOG = n.bit_length()

        g = [[] for _ in range(n + 1)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        depth = [0] * (n + 1)
        up = [[0] * (n + 1) for _ in range(LOG)]

        stack = [(1, 0)]

        while stack:
            u, p = stack.pop()
            up[0][u] = p

            for v in g[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u))

        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[j][i] = up[j - 1][up[j - 1][i]]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a

            d = depth[a] - depth[b]
            j = 0

            while d:
                if d & 1:
                    a = up[j][a]
                d >>= 1
                j += 1

            if a == b:
                return a

            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]

            return up[0][a]

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            x = lca(u, v)
            d = depth[u] + depth[v] - 2 * depth[x]

            ans.append(pow(2, d - 1, MOD))

        return ans