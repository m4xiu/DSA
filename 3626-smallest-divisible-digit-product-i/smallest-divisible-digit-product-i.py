class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            p = 1
            curr = n 
            while curr:
                p *= curr % 10
                curr //= 10
            if p % t == 0: return n
            n += 1