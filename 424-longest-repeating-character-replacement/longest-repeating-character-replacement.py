class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(freq.values())
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
                max_freq = max(freq.values())
            max_len = max(max_len, r - l + 1)
        return max_len


        