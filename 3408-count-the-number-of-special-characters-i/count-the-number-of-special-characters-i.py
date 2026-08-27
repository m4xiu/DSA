class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        ans = 0

        for i in range(26):
            if chr(97 + i) in s and chr(65 + i) in s:
                ans += 1

        return ans