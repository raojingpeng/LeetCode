# Given a binary tree, return the sum of values of its deepest leaves.
#  
# Example 1:
#
#
#
#
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
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
    def __init__(self):
        # DFS 函数不断递归自己 需要在 init 中保存结果
        self.maxdp = -1
        self.total = 0

    def deepestLeavesSum(self, root: TreeNode) -> int:
        # BFS 我自己想的
        # stack = [root]
        # pre = 0
        # end = 0
        # while stack:
        #     tmp = []
        #     pre = end
        #     while stack:
        #         root = stack.pop()
        #         end += root.val
        #         if root.left:
        #             tmp.append(root.left)
        #         if root.right:
        #             tmp.append(root.right)
        #     stack = tmp
        # return end - pre
            
        # BFS 看了官方题解后 自己模仿实现的
        # dq = collections.deque([(root, 0)])
        # maxdp, total = -1, 0
        # while dq:
        #     root, dp = dq.popleft()
        #     if dp > maxdp:
        #         maxdp = dp
        #         total = root.val
        #     elif dp == maxdp:
        #         total += root.val
        #     if root.left:
        #         dq.append((root.left, dp+1))
        #     if root.right:
        #         dq.append((root.right, dp+1))
        # return total

        # DFS 看了官方题解后 自己模仿实现的
        # 空间复杂度比 BFS 稍低
        def dfs(root, depth):
            if root is None:
                return
            if depth > self.maxdp:
                self.maxdp = depth
                self.total = root.val
            elif depth == self.maxdp:
                self.total += root.val
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        
        dfs(root, 0)
        return self.total

                


