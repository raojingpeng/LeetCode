# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # # 递归
        # def helper(root, path):
        #     if root:
        #         path += str(root.val)
        #         if not root.left and not root.right:
        #             ans.append(path)
        #         else:
        #             path += '->'
        #             helper(root.left, path)
        #             helper(root.right, path) 
        
        # ans = []
        # helper(root, '')
        # return ans

        # 迭代
        ans = []
        stack = [(root, '')]
        while stack:
            root, path = stack.pop()
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    ans.append(path)
                else:
                    path += '->'
                    stack.append((root.left, path))
                    stack.append((root.right, path)) 
        return ans
