# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,2,3]
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #  迭代
        # if root is None:
        #     return []
        # result, stack = [], [root]
        # while stack:
        #     root = stack.pop()
        #     result.append(root.val)
        #     if root.right:
        #         stack.append(root.right)
        #     if root.left:
        #         stack.append(root.left)

        # return result

        # 递归
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
