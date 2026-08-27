class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0

        for i in range(len(heights) + 1):
            h = 0 if i == len(heights) else heights[i]

            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                ans = max(ans, height * width)

            stack.append(i)

        return ans