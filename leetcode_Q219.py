# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k

# brute force

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i]==nums[j]) and (abs(i-j)<=k):
                    return True

        return False

# optimised way

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        key_value = {}

        for index, value in enumerate(nums):
            if (value in key_value) and (index-key_value[value]<=k):
                return True

            key_value[value]=index

        return False

