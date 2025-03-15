#  remove duplicates from array

class Solution(object):
    def removeDuplicates(self, nums):
        unique_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]
        return unique_index + 1
