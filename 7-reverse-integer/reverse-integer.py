class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        MIN_INT = -(2**31)      
        MAX_INT = 2**31 - 1     
      
        while x != 0:
            if result < int(MIN_INT / 10) or result > int(MAX_INT / 10):
                return 0
            next_x = int(x / 10)
            digit = x - next_x * 10
            result = result * 10 + digit
            x = next_x
          
        return result
