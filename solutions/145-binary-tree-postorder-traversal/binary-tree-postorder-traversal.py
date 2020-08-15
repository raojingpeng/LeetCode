# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # if not root:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

        # 迭代
        result, stack = [], []
        cur = root

        while cur or stack:
            while cur:  
                stack.append(cur)
                cur = cur.left if cur.left else cur.right  # 从左下开始遍历, 遍历完了从右下开始
            cur = stack.pop()  # 该元素没有左右节点, 一定是根节点
            result.append(cur.val)
            if stack and stack[-1].left == cur:  # 如果stack不为空,且cur是当前栈底元素的左子树
                cur = stack[-1].right
            else:
                cur = None
        return result
