class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, x
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2
            if mid > x // mid:
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1
        if first_true_index == -1:
            return x
        return first_true_index - 1
