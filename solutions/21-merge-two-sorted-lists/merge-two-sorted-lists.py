# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 递归
        # if l1 is None:
        #     return l2
        # if l2 is None:
        #     return l1
        # if l1.val <= l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
        
        # 迭代
        head = ListNode(-1)
        tmp = head
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next

        tmp.next = l1 if l1 else l2
        return head.next

            


