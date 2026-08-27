class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        ch = [[-1] * 26]
        best = [0]
        blen = [10**9]

        for i, w in enumerate(wordsContainer):
            if len(w) < blen[0]:
                best[0] = i
                blen[0] = len(w)

        for i, w in enumerate(wordsContainer):
            node = 0

            for c in w[::-1]:
                x = ord(c) - 97

                if ch[node][x] == -1:
                    ch[node][x] = len(ch)
                    ch.append([-1] * 26)
                    best.append(0)
                    blen.append(10**9)

                node = ch[node][x]

                if len(w) < blen[node]:
                    blen[node] = len(w)
                    best[node] = i

        ans = []

        for w in wordsQuery:
            node = 0
            res = best[0]

            for c in w[::-1]:
                x = ord(c) - 97

                if ch[node][x] == -1:
                    break

                node = ch[node][x]
                res = best[node]

            ans.append(res)

        return ans