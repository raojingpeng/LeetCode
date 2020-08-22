# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
#
# Example 1:
#
#
# Input: s = "leetcode"
# Output: false
#
#
# Example 2:
#
#
# Input: s = "abc"
# Output: true
#
#
#  
#
# Note:
#
#
# 	0 <= len(s) <= 100 
#
#


class Solution:
    def isUnique(self, astr: str) -> bool:
        # if not astr:
        #     return True
        # return Counter(astr).most_common(1)[0][1] < 2

        # return len(set(astr)) == len(astr)

        # 位运算 核心思想是把每个字符用数字代替
        bitmask = 0
        for s in astr:
            move = ord(s) - ord('a')  # 计算距离
            if bitmask & (1 << move) != 0:  # 如果这个位置出现过数字 与元素结果不为0
                return False
            else:
                bitmask |= 1 << move  # 将 bitmask 该位置为1
        return True
