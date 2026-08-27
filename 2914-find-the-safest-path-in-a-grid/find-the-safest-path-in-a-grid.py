from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        dist = [[-1] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dist[i][j] = 0
                    q.append((i, j))

        d = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            i, j = q.popleft()

            for di, dj in d:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < n and dist[x][y] == -1:
                    dist[x][y] = dist[i][j] + 1
                    q.append((x, y))

        heap = [(-dist[0][0], 0, 0)]
        seen = set()

        while heap:
            safe, i, j = heapq.heappop(heap)
            safe = -safe

            if (i, j) in seen:
                continue

            seen.add((i, j))

            if i == n - 1 and j == n - 1:
                return safe

            for di, dj in d:
                x, y = i + di, j + dj

                if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
                    heapq.heappush(
                        heap,
                        (-min(safe, dist[x][y]), x, y)
                    )

        return 0