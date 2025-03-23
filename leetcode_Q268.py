# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# method 1:-

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n+1):
            if i not in nums:
                return i

# method 2 optimised way:-

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n= len(nums)

        expected_sum = (n*(n+1))//2
        actual_sum = sum(nums)

        return expected_sum-actual_sum
