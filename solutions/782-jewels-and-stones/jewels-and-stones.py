# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
#
# Example 1:
#
#
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
#
#
# Example 2:
#
#
# Input: J = "z", S = "ZZ"
# Output: 0
#
#
# Note:
#
#
# 	S and J will consist of letters and have length at most 50.
# 	The characters in J are distinct.
#
#


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # 暴力法 i in S 相当于遍历 S
        # 时间复杂度 O(len(j)*len(S))
        # 空间复杂度 O(1)      
        # return sum(i in J for i in S)

        # 哈希法
        # 时间复杂度 O(len(J)+len(S)) len(J) 来源于创建J
        # 空间复杂度 O(len(J))
        J = set(J)
        return sum(i in J for i in S)
