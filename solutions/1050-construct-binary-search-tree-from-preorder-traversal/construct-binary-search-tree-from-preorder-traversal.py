# Return the root node of a binary search tree that matches the given preorder traversal.
#
# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
#
# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.
#
# Example 1:
#
#
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
#
#
#
#  
# Constraints:
#
#
# 	1 <= preorder.length <= 100
# 	1 <= preorder[i] <= 10^8
# 	The values of preorder are distinct.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # 递归
        # def helper(lower=float('-inf'), upper=float('inf')):
        #     nonlocal index
        #     if index > _len:
        #         return None
        #     value = preorder[index]
        #     if value < lower or value > upper:
        #         return None
        #     index += 1
        #     root = TreeNode(value)
        #     root.left = helper(lower, value)
        #     root.right = helper(value, upper)
        #     return root

        # index = 0
        # _len = len(preorder)-1
        # return helper()

        # 迭代
        # root = TreeNode(preorder[0])
        # stack = [root,]

        # for i in range(1, len(preorder)):
        #     node, child = stack[-1], TreeNode(preorder[i])
        #     while stack and stack[-1].val < child.val:
        #         node = stack.pop()
            
        #     if node.val < child.val:
        #         node.right = child
        #     else:
        #         node.left = child
        #     stack.append(child)
        # return root

        # 递归2 （类似快排序 好理解 但是性能差）
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        left , right = [], []
        for i in preorder[1:]:
            if root.val > i:
                left.append(i)
            else:
                right.append(i)
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        return root
