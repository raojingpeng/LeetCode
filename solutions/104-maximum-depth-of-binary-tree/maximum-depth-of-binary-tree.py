# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its depth = 3.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 迭代 根据官方的稍微精简了下代码
        stack = [(root, 1)]
        depth = 0
        while stack:
            root, dp = stack.pop()
            if root is not None:
                depth = max(dp, depth)
                stack.append((root.left, dp+1))
                stack.append((root.right, dp+1))
        return depth

        # # 递归 是神
        # if root is None:
        #     return 0  # 递归终止条件
        # # 递归条件：求根节点最大深度就等于求他左节点最大深度与右节点最大深度中的最大值+1
        # left = self.maxDepth(root.left) + 1
        # right = self.maxDepth(root.right) + 1
        # return max(left, right)

