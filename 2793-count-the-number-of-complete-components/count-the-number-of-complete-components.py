class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            nodes = 1
            edge_count = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    a, b = dfs(nei)
                    nodes += a
                    edge_count += b

            return nodes, edge_count

        for i in range(n):
            if not visited[i]:
                nodes, edges_count = dfs(i)

                if edges_count == nodes * (nodes - 1):
                    ans += 1

        return ans