class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        cumsum_to_index = {0: 0}

        cumulative_sum = 0
        array_length = len(arr)
        min_length = [float('inf')] * (array_length + 1)
        min_total_length = float('inf')

        for current_index, current_value in enumerate(arr, 1):
            cumulative_sum += current_value
            min_length[current_index] = min_length[current_index - 1]
            required_sum = cumulative_sum - target

            if required_sum in cumsum_to_index:
                start_index = cumsum_to_index[required_sum]
                current_subarray_length = current_index - start_index
                min_length[current_index] = min(min_length[current_index], current_subarray_length)
                combined_length = min_length[start_index] + current_subarray_length
                min_total_length = min(min_total_length, combined_length)
            cumsum_to_index[cumulative_sum] = current_index
        return -1 if min_total_length > array_length else min_total_length
