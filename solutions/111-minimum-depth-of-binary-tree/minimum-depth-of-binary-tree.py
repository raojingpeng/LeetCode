# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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
# return its minimum depth = 2.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):驾驶证&行驶证-旋转
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # BFS 保证了最先搜索到的叶子节点的深度一定最小
        # if not root:
        #     return 0
        # stack = deque([(root, 1)])
        # while stack:
        #     root, depth = stack.popleft()
        #     if root.left is None and root.right is None:
        #         return depth
        #     if root.left:
        #         stack.append((root.left, depth+1))
        #     if root.right:
        #         stack.append((root.right, depth+1))

        # DFS 对于每一个非叶子节点 我们只需要分别计算其左右子树的最小叶子节点深度,就能把一个大问题转换成小问题,可以递归的解决该问题
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

