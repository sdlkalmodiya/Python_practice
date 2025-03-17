# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.
# method 1

class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left<=right):
            if target<=nums[left]:
                return left
            elif target>nums[right]:
                return right+1
            elif target==nums[right]:
                return right
            elif nums[left]<target<nums[right]:
                left += 1

# method 2 (binary search)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            # Insertion index candidate
            mid = (left+right)//2
            # Target too large, search right
            if target> nums[mid]: left = mid+1
            # Target too small, search left
            else: right = mid-1
        return left
            
        
