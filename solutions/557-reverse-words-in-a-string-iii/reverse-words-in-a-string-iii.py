# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
#
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
#
#
# Note:
# In the string, each word is separated by single space and there will not be any extra space in the string.
#


class Solution:
    def reverseWords(self, s: str) -> str:
        # 一行完事
        # return ' '.join(i[::-1] for i in s.split())

        # 看题解里有人用栈去做, 我也尝试下
        ans = ''
        stack = []
        s += ' '
        for i in s:
            stack.append(i)
            if i == ' ':
                while stack:
                    ans += stack.pop()

        return ans[1:]
        
