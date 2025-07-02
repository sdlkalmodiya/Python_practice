# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]

 """ its time complexity is high o(n^2) as we are iterating through complete list for each element"""
             
# if sorted array is given then we can use two pointer method

""" its time complexity is only o(n) as we are iterating once only through list"""

class Solution(object):
    def twoSum(self, nums, target):
        left,right = 0, len(nums)-1
        while(left<right):
            if nums[left]+nums[right] == target:
                return [left, right]
            elif nums[left]+nums[right] > target:
                right -= 1
            elif nums[left]+nums[right] < target:
                left +=1

# Most Optimised way is to use hash map when we have to deal with index of numbers in an array

class Solution(object):
    def twoSum(self, nums, target):
        
        hash_map = {}
        for index, element in enumerate(nums):
            find_element = target-element
            if find_element in hash_map:
                return[hash_map[find_element], index]
            hash_map[element] = index

