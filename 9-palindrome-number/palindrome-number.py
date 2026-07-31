class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        Reversed_num = 0 
        temp = x

        while temp > 0:
            Reversed_num = Reversed_num * 10 + temp % 10
            temp //= 10

        return x == Reversed_num