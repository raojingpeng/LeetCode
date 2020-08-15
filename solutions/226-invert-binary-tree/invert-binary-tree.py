# Invert a binary tree.
#
# Example:
#
# Input:
#
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# Output:
#
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 递归
        # if not root:
        #     return root
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        # 迭代
        if not root:
            return root

        stack = [root]
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return root
        

