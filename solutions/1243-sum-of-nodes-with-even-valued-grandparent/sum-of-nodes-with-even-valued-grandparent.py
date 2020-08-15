# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)
#
# If there are no nodes with an even-valued grandparent, return 0.
#
#  
# Example 1:
#
#
#
#
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is between 1 and 10^4.
# 	The value of nodes is between 1 and 100.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def __init__(self):
    #     self.total = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # 我的反思: 没有想到存祖父节点的值
        # 虽然Ac了 但是方法比较笨
        # BFS
        # if root.val % 2 == 0:
        #     if root.left:
        #         if root.left.left:
        #             self.total += root.left.left.val
        #         if root.left.right:
        #             self.total += root.left.right.val
        #         self.sumEvenGrandparent(root.left)
        #     if root.right:
        #         if root.right.left:
        #             self.total += root.right.left.val
        #         if root.right.right:
        #             self.total += root.right.right.val
        #         self.sumEvenGrandparent(root.right)
        # else:
        #     if root.left:
        #         self.sumEvenGrandparent(root.left)
        #     if root.right:
        #         self.sumEvenGrandparent(root.right)
        # return self.total 

        # DFS 参考官方 （最佳方法）
        # total = 0
        # def dfs(grandparent, parent, node):
        #     if node is None:
        #         return
        #     if grandparent % 2 == 0:
        #         nonlocal total
        #         total += node.val
        #     dfs(parent, node.val, node.left)
        #     dfs(parent, node.val, node.right)
        
        # dfs(1, 1, root)
        # return total

        # BFS 参考官方（跟我的思路类似）
        q = collections.deque([root])
        total = 0
        while q:
            root = q.popleft()
            if root.val % 2 == 0:
                if root.left:
                    if root.left.left:
                        total += root.left.left.val
                    if root.left.right:
                        total += root.left.right.val
                if root.right:
                    if root.right.left:
                        total += root.right.left.val
                    if root.right.right:
                        total += root.right.right.val
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        
        return total
