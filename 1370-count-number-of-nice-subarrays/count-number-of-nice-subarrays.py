class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:


        l = 0
        r = 0
        sum = 0
        count = 0

        while r < len(nums):
            sum += nums[r] % 2

            while sum > k:
                sum -= nums[l] % 2
                l += 1

            count += r - l + 1
            r += 1

        first = count

        l = 0
        r = 0
        sum = 0
        count = 0
        k -= 1

        if k < 0:
            return first

        while r < len(nums):
            sum += nums[r] % 2

            while sum > k:
                sum -= nums[l] % 2
                l += 1

            count += r - l + 1
            r += 1

        return first - count
        