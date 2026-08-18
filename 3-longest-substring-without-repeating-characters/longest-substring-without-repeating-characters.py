class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {} # char -> last index
        start = 0
        res = 0
        for end, char in enumerate(s):
            # If the char was seen and its last index is within the current window
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            res = max(res, end - start + 1)
            last_seen[char] = end
        return res