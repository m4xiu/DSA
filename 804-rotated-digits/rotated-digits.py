class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0

        for x in range(1, n + 1):
            changed = False

            for c in str(x):
                if c in "347":
                    break
                if c in "2569":
                    changed = True
            else:
                if changed:
                    ans += 1

        return ans