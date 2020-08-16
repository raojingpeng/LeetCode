# Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n pairs of parentheses.
#
# Note: The result set should not contain duplicated subsets.
#
# For example, given n = 3, the result should be:
#
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#
#


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        cur_str = ''
        # 深度优先搜索（回溯）+ 剪枝
        def dfs(cur_str, left, right):
            if left == 0 and right == 0:
                ans.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left -1 , right)
            if right > 0:
                dfs(cur_str + ')', left, right -1)
        
        dfs(cur_str, n, n)
        return ans
