class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
      
        def find_unique_boundary_value(position: int) -> int:
            for index, value in enumerate(nums):
                if index != position and value == nums[position]:
                    return -1  
            return nums[position]  
      
        if k == 1:
            from collections import Counter
            frequency_map = Counter(nums)
            unique_values = (value for value, count in frequency_map.items() if count == 1)
            return max(unique_values, default=-1)
      
        if k == len(nums):
            return max(nums)

        first_position_value = find_unique_boundary_value(0)
        last_position_value = find_unique_boundary_value(len(nums) - 1)
        return max(first_position_value, last_position_value)
      