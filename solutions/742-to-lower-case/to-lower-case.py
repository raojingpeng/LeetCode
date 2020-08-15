# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
#
#  
#
#
# Example 1:
#
#
# Input: "Hello"
# Output: "hello"
#
#
#
# Example 2:
#
#
# Input: "here"
# Output: "here"
#
#
#
# Example 3:
#
#
# Input: "LOVELY"
# Output: "lovely"
#
#
#
#


class Solution:
    def toLowerCase(self, str: str) -> str:
        # return str.lower()

        # 大小写字母ASCII值差32，利用ord()函数即可
        ans = ''
        for i in str:
            if i >= 'A' and i <= 'Z':
                ans += chr(ord(i) + 32)
            else:
                ans += i
        return ans
