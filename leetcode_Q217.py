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

# optimised way using hashmap

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        key_value = {}

        for i in nums:
            if i in key_value.keys():
                key_value[i] = key_value[i] + 1

            else:
                key_value[i] = 1
            
        set_tmp = set(key_value.values())
        if len(set_tmp) == 1:
            return False

        else:
            return True
            
