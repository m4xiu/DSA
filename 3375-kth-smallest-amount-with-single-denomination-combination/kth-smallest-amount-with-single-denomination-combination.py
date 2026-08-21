class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count_multiples_up_to(max_value: int) -> int:
            total_count = 0

            for subset_mask in range(1, 1 << len(coins)):
                lcm_value = 1

                for coin_index, coin_value in enumerate(coins):
                    if subset_mask >> coin_index & 1:
                        lcm_value = lcm(lcm_value, coin_value)
                        if lcm_value > max_value:
                            break

                subset_size = subset_mask.bit_count()
                if subset_size & 1:
                    total_count += max_value // lcm_value
                else:
                    total_count -= max_value // lcm_value

            return total_count

        def feasible(mid: int) -> bool:

            return count_multiples_up_to(mid) >= k


        left, right = 1, 10**11
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return first_true_index
