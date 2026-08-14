class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = "".join(map(str, digits))
        incremented_str = str(int(num_str) + 1)
        return [int(char) for char in incremented_str]