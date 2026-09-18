class Solution:
    def maxNumOfSubstrings(self, s: str):
        first = [len(s)] * 26
        last = [-1] * 26

        for i, c in enumerate(s):
            x = ord(c) - 97
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        for c in range(26):
            l = first[c]
            r = last[c]

            if r == -1:
                continue

            i = l
            while i <= r:
                x = ord(s[i]) - 97
                if first[x] < l:
                    break
                r = max(r, last[x])
                i += 1
            else:
                intervals.append((r, l))

        intervals.sort()

        ans = []
        end = -1

        for r, l in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans