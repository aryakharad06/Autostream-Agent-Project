class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:

        def atMost(k):
            freq = {}
            l = 0
            r = 0
            count = 0

            while r < len(nums):
                freq[nums[r]] = freq.get(nums[r], 0) + 1

                while len(freq) > k:
                    freq[nums[l]] -= 1

                    if freq[nums[l]] == 0:
                        del freq[nums[l]]

                    l += 1

                count += r - l + 1
                r += 1

            return count

        return atMost(k) - atMost(k - 1)