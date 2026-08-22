class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        temp_n = n
      
        while temp_n > 0:
            temp_n, digit = divmod(temp_n, 10)
          
            digit_sum += digit
            digit_product *= digit
        return n % (digit_sum + digit_product) == 0