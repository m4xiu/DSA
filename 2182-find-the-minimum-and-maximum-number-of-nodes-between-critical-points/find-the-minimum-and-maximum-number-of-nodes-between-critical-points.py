from typing import List, Optional
from math import inf

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_distance = inf
        max_distance = -inf
        first_critical_point = -1
        last_critical_point = -1
        current_position = 0

        while head.next and head.next.next:
            previous_val = head.val
            current_val = head.next.val
            next_val = head.next.next.val
          
            is_local_minimum = previous_val > current_val < next_val
            is_local_maximum = previous_val < current_val > next_val
          
            if is_local_minimum or is_local_maximum:
                if last_critical_point == -1:
                    # First critical point found
                    first_critical_point = current_position
                    last_critical_point = current_position
                else:
                    min_distance = min(min_distance, current_position - last_critical_point)
                  
                    last_critical_point = current_position

                    max_distance = max(max_distance, last_critical_point - first_critical_point)
          
            # Move to the next position
            current_position += 1
            head = head.next

        if first_critical_point == last_critical_point:
            return [-1, -1]
        else:
            return [min_distance, max_distance]
