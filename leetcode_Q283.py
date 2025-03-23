# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = 0
        
        for left in range(len(nums)):
            if nums[left] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                right += 1
