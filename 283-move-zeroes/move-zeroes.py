class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp = []
        for i in range(len(nums)):
            if nums [i] != 0:
                temp.append(nums[i])

        
        for i in range(len(temp)):
            nums[i] = temp[i]
        for i in range(len(temp), len(nums)):
            nums[i] = 0


        """
        Do not return anything, modify nums in-place instead.
        """
        