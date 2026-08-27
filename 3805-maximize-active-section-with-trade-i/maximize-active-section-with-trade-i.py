class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ans = 0
        pre = -10**9
        mx = 0
        i = 0

        while i < len(s):
            j = i

            while j < len(s) and s[j] == s[i]:
                j += 1

            cur = j - i

            if s[i] == '1':
                ans += cur
            else:
                mx = max(mx, pre + cur)
                pre = cur

            i = j

        return ans + mx