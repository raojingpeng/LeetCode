# Given an array of integers nums, sort the array in ascending order.
#
#  
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 50000
# 	-50000 <= nums[i] <= 50000
#
#


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        point = nums[0]
        left, right = [], []
        for i in nums[1:]:
            if i < point:
                left.append(i)
            else:
                right.append(i)
        
        return self.sortArray(left) + [point] + self.sortArray(right)

