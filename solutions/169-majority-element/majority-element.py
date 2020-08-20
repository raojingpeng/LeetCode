# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 核心是众数出现次数大于数组长度的一半
        # 方法一 哈希表 O(n) O(n)
        # from collections import Counter
        # return Counter(nums).most_common(1)[0][0]
        # 方法二 排序 取中间元素 O(nlogn) O(logn)
        # return sorted(nums)[len(nums)//2]
        # 方法三 随机数 O(n) O(1)
        # import random
        # while True:
        #     num = random.choice(nums)
        #     if sum(1 for i in nums if i == num) > len(nums) // 2:
        #         return num
        # 方法四 投票算法 核心思路是对拼消耗(诸侯争霸的例子) O(n) O(1)
        choice = None
        count = 0
        for i in nums:
            if count == 0:
                choice = i
            if i == choice:
                count += 1
            else:
                count -= 1
        return choice

