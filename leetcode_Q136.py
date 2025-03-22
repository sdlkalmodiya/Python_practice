# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# method 1 

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = 0
        unique = nums[left]
        while(left<len(nums) and right<len(nums)):
            if left==right:
                right+=1

            elif nums[left] == nums[right]:
                left+=1
                right=0
                unique = nums[left]

            else:
                right+=1

        return unique


# optimised method

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()

        for i in range(0, len(nums)-1, 2):
                if nums[i] != nums[i+1]:  
                    return nums[i]
        return nums[-1]
                
                
