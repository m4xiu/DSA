from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        sr = sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        total = len(litter)

        if total == 0:
            return 0

        target = (1 << total) - 1

        q = deque()
        q.append((sr, sc, energy, 0, 0))

        seen = {(sr, sc, energy, 0)}

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, e, mask, moves = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1

                # Can't move with no energy unless arriving at R
                if ne < 0:
                    continue

                nmask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    nmask |= 1 << litter[(nr, nc)]

                # Reset energy
                if classroom[nr][nc] == 'R':
                    ne = energy

                if nmask == target:
                    return moves + 1

                state = (nr, nc, ne, nmask)

                if state not in seen:
                    seen.add(state)
                    q.append((nr, nc, ne, nmask, moves + 1))

        return -1