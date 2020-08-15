# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # if not root:
        #     return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        # 迭代
        if not root:
            return []
        
        result, stack = [], []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result
