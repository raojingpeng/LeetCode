# English description is not available for the problem. Please switch to Chinese.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # 递归
        # if not root:
        #     return
        # root.left, root.right = root.right, root.left
        # self.mirrorTree(root.left)
        # self.mirrorTree(root.right)
        # return root

        # 迭代 比上次写得有进步(https://leetcode-cn.com/problems/invert-binary-tree)
        stack = [root]
        while stack:
            head = stack.pop()
            if not head:
                continue
            head.left, head.right = head.right, head.left
            stack.append(head.left)
            stack.append(head.right)

        return root
