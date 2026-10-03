class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        n = len(s)
        last_seen = [-1, -1, -1]
        count = 0
        for i in range(n):
            last_seen[ord(s[i]) - ord('a')] = i
            if min(last_seen) != -1:
                count += min(last_seen) + 1
        return count

        