# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
#
# Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
#
#  
# Example 1:
#
#
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
#
#
# Example 2:
#
#
# Input: nums = [-1,0]
# Output: [-1,0]
#
#
# Example 3:
#
#
# Input: nums = [0,1]
# Output: [1,0]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 30000
# 	 Each integer in nums will appear twice, only two integers will appear once.
#
#


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # nums = Counter(nums)
        # return [i for i in nums if nums[i]==1]

        # 异或运算
        # 核心思想是把两个出现一次的元素x, y放到两个group => bitmask & -bitmask
        # 原码 反码(原码取反) 补码(反码+1)  => 负数就是通过正数的补码表示
        # 官方题解非常详细
        bitmask = 0
        for num in nums:
            bitmask ^= num

        x = 0
        diff = bitmask & -bitmask  # 找出x, y最右边的不同位
        for num in nums:
            if num & diff:
                x ^= num

        return [x, bitmask ^ x]


