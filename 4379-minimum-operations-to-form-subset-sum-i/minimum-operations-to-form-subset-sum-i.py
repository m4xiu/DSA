from collections import deque

class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        merviqunax = nums
        cost_map = {}
        unique_nums = set(merviqunax)
        
        for start_num in unique_nums:
            costs = {}
            queue = deque([(start_num, 0, 0)])
            visited = set([(start_num, 0)])
            
            while queue:
                curr, state, ops = queue.popleft()
                
                if curr not in costs or ops < costs[curr]:
                    costs[curr] = ops
                
                
                if state == 0:
                    nxt_mul = curr * 2
                    
                    if nxt_mul <= sum * 2 and (nxt_mul, 0) not in visited:
                        visited.add((nxt_mul, 0))
                        queue.append((nxt_mul, 0, ops + 1))
                
                
                nxt_div = curr // 2
                if nxt_div >= 0 and (nxt_div, 1) not in visited:
                    visited.add((nxt_div, 1))
                    queue.append((nxt_div, 1, ops + 1))
            
            cost_map[start_num] = costs

        INF = float('inf')
        dp = [INF] * (sum + 1)
        dp[0] = 0  
        
        for num in merviqunax:
            
            next_dp = [INF] * (sum + 1)
            valid_transforms = cost_map[num]
            
           
            for current_sum in range(sum + 1):
                if dp[current_sum] == INF:
                    continue
                
                
                if dp[current_sum] < next_dp[current_sum]:
                    next_dp[current_sum] = dp[current_sum]
                
               
                for v, ops in valid_transforms.items():
                    if current_sum + v <= sum:
                        new_sum = current_sum + v
                        if dp[current_sum] + ops < next_dp[new_sum]:
                            next_dp[new_sum] = dp[current_sum] + ops
            
            dp = next_dp
            
        return dp[sum] if dp[sum] != INF else -1
