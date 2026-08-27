class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        mod = 10**9 + 7

        score = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        score[n-1][n-1] = 0
        ways[n-1][n-1] = 1

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X' or (i == n-1 and j == n-1):
                    continue

                for x, y in ((i+1,j), (i,j+1), (i+1,j+1)):
                    if x < n and y < n and score[x][y] != -1:
                        if score[x][y] > score[i][j]:
                            score[i][j] = score[x][y]
                            ways[i][j] = ways[x][y]
                        elif score[x][y] == score[i][j]:
                            ways[i][j] = (ways[i][j] + ways[x][y]) % mod

                if score[i][j] != -1 and board[i][j].isdigit():
                    score[i][j] += int(board[i][j])

        if score[0][0] == -1:
            return [0, 0]

        return [score[0][0], ways[0][0] % mod]