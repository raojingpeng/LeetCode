# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
#  
# Example 1:
#
#
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
#
#
# Example 2:
#
#
# Input: head = []
# Output: []
#
#
# Example 3:
#
#
# Input: head = [0]
# Output: [0]
#
#
# Example 4:
#
#
# Input: head = [1,3]
# Output: [3,1]
#
#
#  
# Constraints:
#
#
# 	The numner of nodes in head is in the range [0, 2 * 10^4].
# 	-10^5 <= Node.val <= 10^5
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 这道题类似 108. 将有序数组转换为二叉搜索树
        # 108 题是升序数组，求中间节点使用数学方法就可以了
        # 这道题是链表，求中间节点需要使用快慢指针，快指针移动距离是慢指针的两倍
        # 精髓是使用 pre 记录中间节点的前一个节点，并将该节点与中间节点「剪断」，便于计算左节点
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        p, q, pre = head, head, None
        while q and q.next:
            pre = p
            p = p.next
            q = q.next.next
        pre.next = None
        root = TreeNode(p.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(p.next)
        return root


