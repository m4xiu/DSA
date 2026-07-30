class Solution:
    def maxProduct(self, n: int) -> int:
        d = []

        while n:
            d.append(n % 10)
            n//=10
        d.sort()
        return d[-1] * d[-2]

