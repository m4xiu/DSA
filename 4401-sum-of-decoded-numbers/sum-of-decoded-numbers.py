class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        vornelqati = nums
        MOD = 10**9 + 7
        total_sum = 0
        
        for num in vornelqati:
            width = num % 10
            d = num // 10
            d_str = str(d)

            x_str = d_str[:width]
            y_str = d_str[width:]
            

            x = int(x_str)
            y = int(y_str)
            
            decoded_value = pow(x, y, MOD)
            total_sum = (total_sum + decoded_value) % MOD
            
        return total_sum
