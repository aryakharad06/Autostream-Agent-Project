class Solution:
    def trap(self, height: list[int]) -> int:
        lmax = 0
        rmax = 0
        total = 0
        l = 0
        r = len(height) - 1
        
        while l <= r:
            if height[l] <= height[r]:
                if height[l] > lmax:
                    lmax = height[l]
                else: 
                    total += lmax - height[l]
                l = l + 1
            else :
                if rmax > height[r]:
                    total += rmax - height[r]
                else :
                    rmax = height[r]
                r = r - 1
        return total






        
         
        