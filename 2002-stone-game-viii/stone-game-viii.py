class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix_sums = list(accumulate(stones))
      
        @cache
        def calculate_max_score_difference(current_index: int) -> int:
           
            if current_index >= len(stones) - 1:
                return prefix_sums[-1]
            skip_current = calculate_max_score_difference(current_index + 1)

            take_current = prefix_sums[current_index] - calculate_max_score_difference(current_index + 1)
            return max(skip_current, take_current)
      
        
        return calculate_max_score_difference(1)
