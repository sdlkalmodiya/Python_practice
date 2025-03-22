# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        n = len(nums)
        if n%2==0:
            index = len(nums)//2 - 1
            return nums[index]
        
        else:
            index = len(nums)//2 
            return nums[index]
