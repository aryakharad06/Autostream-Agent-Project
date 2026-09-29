class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        lsum = 0
        for i in range(k):
            lsum += cardPoints[i]
        maxsum = lsum
        for i in range(k):
            lsum -= cardPoints[k - 1 - i]

            lsum += cardPoints[n - 1 - i] 
            
            maxsum = max(maxsum, lsum)
        return maxsum    



        