# English description is not available for the problem. Please switch to Chinese.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 递归
        # if not root: return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        # bfs
        depth = 0
        stack = [(root, 1)]
        while stack:
            root, cur_depth = stack.pop()
            if root:
                depth = max(depth, cur_depth)
                stack.append((root.left, cur_depth+1))
                stack.append((root.right, cur_depth+1))
        return depth


