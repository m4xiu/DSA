class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        seen = set()
        invalid = set()
        current = None
        
        for num in nums:
            if num != current:
                if num in seen:
                    invalid.add(num)
                seen.add(num)
                current = num
                
        return len(seen) - len(invalid)
