# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # substr = ""
        # if not strs:
        #     return substr
        # for j in range(min(len(i) for i in strs)):
        #     flag = strs[0][j]
        #     if all(k[j]==flag for k in strs[1:]):
        #         substr += flag
        #     else:
        #         return substr
        
        # return substr

        # 方法2 zip + 解引用
        substr = ""
        for i in zip(*strs):
            if len(set(i)) != 1:
                return substr
            substr += i[0]
        return substr


