class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        max_area = 0
        heights = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    heights[j] += 1
                    
                else:
                    heights[j] = 0
            int_area = self.largestRectangleArea(heights)
            max_area = max(max_area, int_area)
        return max_area
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




        
                
                






        