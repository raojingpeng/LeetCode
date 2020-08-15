#
# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
#
#
# Example:
#
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#
#
#
# Restrictions: 
#
#  The string consists of lower English letters only.
#  Length of the given string and k will in the range [1, 10000]
#


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 自己想的
        # ans = ''
        # i = 0
        # while i + k * 2 <= len(s):
        #     ans += s[i:i + k][::-1] + s[i + k:i + k * 2]
        #     i += k * 2
        # remain = len(s) - i
        # if remain < k:
        #     ans += s[i:][::-1]
        # elif k <= remain < 2 * k:
        #     ans += s[i:i + k][::-1] + s[i + k:]
        # return ans

        # 理解题意以后
        ans = ''
        for i in range(0, len(s), 2*k):
            ans += s[i:i+k][::-1] + s[i+k:i+k*2]

        return ans


