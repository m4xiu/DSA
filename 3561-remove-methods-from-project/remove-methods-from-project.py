class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        edges = [[]for _ in range(n)]
        in_degree = [0] * n

        for u,v in invocations:
            edges[u].append(v)
            in_degree[v] += 1

        queue = collections.deque([k])
        suspicious = bytearray(n)
        suspicious[k] = 1

        while queue:
            u = queue.popleft()
            for v in edges[u]:
                in_degree[v] -= 1

                if suspicious[v] == 0:
                    queue.append(v)
                    suspicious[v] = 1
                    
        can_remove_all = True
        for i in range(n):
            if suspicious[i] == 1 and in_degree[i] > 0:
                   can_remove_all = False
                   break

        if can_remove_all:
            return [i for i in range(n) if suspicious[i] == 0]
        else:
            return list(range(n))