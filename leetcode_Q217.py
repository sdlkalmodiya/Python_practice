# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
            
        return False
