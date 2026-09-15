class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        nse = [n] * n
        pse = [-1] * n
        stack = []
        total = 0
        MOD = 10**9 + 7

        #pse
        stack = []
        for i in range(n):
            
            
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
        
        #nse
        stack = []
        for i in range(n - 1, -1, -1):
            
            
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]

            stack.append(i) 
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i

            total += left * right * arr[i]
            total %= MOD   
        return total
            

        