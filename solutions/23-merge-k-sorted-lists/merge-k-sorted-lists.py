# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)
        tmp = head
        lists = [i for i in lists if i]
        val_list = [i.val for i in lists]

        while lists:
            index = val_list.index(min(val_list))
            tmp.next = lists[index]
            tmp = tmp.next
            if lists[index].next:
                lists[index] = lists[index].next
                val_list[index] = lists[index].val
            else:
                lists.pop(index)
                val_list.pop(index)
        return head.next

