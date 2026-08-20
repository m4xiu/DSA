class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for current_element in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(current_element)
            else:
                arr2.append(current_element)
        return arr1 + arr2