class Solution:
    def smallestIndex(self, nums):
        for i, x in enumerate(nums):
            if sum(map(int, str(x))) == i:
                return i
        return -1