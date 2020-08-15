# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
#
# You have to form a team of 3 soldiers amongst them under the following rules:
#
#
# 	Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# 	A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
#
#
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
#
#  
# Example 1:
#
#
# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
#
#
# Example 2:
#
#
# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.
#
#
# Example 3:
#
#
# Input: rating = [1,2,3,4]
# Output: 4
#
#
#  
# Constraints:
#
#
# 	n == rating.length
# 	1 <= n <= 200
# 	1 <= rating[i] <= 10^5
#


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # 枚举三元组 时间复杂度O(n三次方)
        # ans = 0
        # for i in range(len(rating)):
        #     for j in range(i+1, len(rating)):
        #         for k in range(j+1, len(rating)):
        #             if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
        #                 ans += 1
        # return ans

        # 枚举中间点 时间复杂度O(n的平方)
        # 关键点在于对点j来说 jless*kmore + jmore * kless
        # 有点二分法的感觉 选取哨兵节点, 比哨兵节点小的放左边, 大的放右边?
        ans = 0
        for i in range(1, len(rating)-1):
            jless = jmore = kless = kmore = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    jless += 1
                elif rating[j] > rating[i]:
                    jmore += 1
            for k in range(i+1, len(rating)):
                if rating[k] < rating[i]:
                    kless += 1
                elif rating[k] > rating[i]:
                    kmore += 1
            ans += jless * kmore + jmore * kless
        return ans






