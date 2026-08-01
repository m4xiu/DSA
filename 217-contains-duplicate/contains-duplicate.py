class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hasht = set()
        for num in nums:
            if num in hasht:
                return True
            else:
                hasht.add(num)
        return False