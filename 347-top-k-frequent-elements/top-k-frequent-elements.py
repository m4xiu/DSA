class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter = Counter(nums)
        most_common_elements = frequency_counter.most_common(k)
        result = [element for element, count in most_common_elements]
      
        return result