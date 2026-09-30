class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        r = 0
        max_len = 0
        zeros = 0
        
        
        while r < len(nums):
            if nums[r] == 0:

                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
        
                    



            

