class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        
        l = 0
        r = 0
        sum = 0
        count = 0
        
        while r < len(nums):
            sum += nums[r]
            while sum > goal:
                sum -= nums[l]
                l += 1
            count += r - l + 1
            r += 1
        first = count

        l = 0
        r = 0
        sum = 0
        count = 0
        goal -= 1
        if goal < 0:
            return first
        while r < len(nums):
            sum += nums[r]
            while sum > goal:
                sum -= nums[l]
                l += 1
            count += r - l + 1
            r += 1
        return first - count
