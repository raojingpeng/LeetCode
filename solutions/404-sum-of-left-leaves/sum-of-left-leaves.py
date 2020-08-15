# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # BFS
        ans = 0
        stack = [root]
        while stack:
            root = stack.pop(0)
            if root is None:
                continue
            if root.left and not root.left.left and not root.left.right:
                ans += root.left.val
            stack.append(root.left)
            stack.append(root.right)
        return ans

        # DFS
        # ans = 0
        # def dfs(root):
        #     if not root:
        #         return
        #     nonlocal ans
        #     if root.left and not root.left.left and not root.left.right:
        #         ans += root.left.val
        #     dfs(root.left)
        #     dfs(root.right)
        #
        # dfs(root)
        # return ans


