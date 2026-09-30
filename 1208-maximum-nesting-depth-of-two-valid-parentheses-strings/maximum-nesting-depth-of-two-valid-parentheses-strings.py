class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result = [0] * len(seq)
        depth = 0
        for index, char in enumerate(seq):
            if char == "(":
                result[index] = depth & 1
                depth += 1
            else: 
                depth -= 1
                result[index] = depth & 1
      
        return result
