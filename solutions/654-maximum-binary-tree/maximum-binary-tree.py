#
# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#
# The root is the maximum number in the array. 
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number. 
#
#
#
#
# Construct the maximum tree by the given array and output the root node of this tree.
#
#
# Example 1:
#
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#
#       6
#     /   \
#    3     5
#     \    / 
#      2  0   
#        \
#         1
#
#
#
# Note:
#
# The size of the given array will be in the range [1,1000].
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # 递归套路三部曲
        # 1. 递归终止条件: nums 长度为 0
        # 2. 返回什么: 返回构造好了的二叉树根节点(最大节点)
        # 3. 本次递归做了什么: 根据根节点将数组划分为左右两段,分别构造左右子树
        if not nums:
            return None

        index = 0
        for i in range(len(nums)):
            if nums[i] > nums[index]:
                index = i
        
        head = TreeNode(nums[index])
        head.left = self.constructMaximumBinaryTree(nums[:index])
        head.right = self.constructMaximumBinaryTree(nums[index+1:])
        return head
