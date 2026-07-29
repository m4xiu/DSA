class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PrevMap = {} #Val : index

        for i, n in enumerate(nums):
            diff = target -n
            if diff in PrevMap:
                return [PrevMap[diff],i]
            PrevMap[n]=i
        return
        