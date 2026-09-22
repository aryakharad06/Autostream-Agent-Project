class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int: 
        stack = []
        max_area = 0
        height = 0
        for i in range (len(heights)):
            while stack and heights[stack[-1]] > heights[i]:

                height = heights[stack.pop()]
                
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        while stack:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = len(heights) - left - 1
                max_area = max(max_area, height * width)
        return max_area




        