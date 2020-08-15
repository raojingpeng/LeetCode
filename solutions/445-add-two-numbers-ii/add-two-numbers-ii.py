# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
#
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 反转链表 比较麻烦 不建议使用
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     def reverse_list_node(n):
    #         pre = None
    #         while n:
    #             tmp = n.next
    #             n.next = pre
    #             pre = n
    #             n = tmp
    #         return pre

    #     l1 = reverse_list_node(l1)
    #     l2 = reverse_list_node(l2)

    #     l = None
    #     carry = 0
    #     while l1 or l2 or carry:
    #         x = l1.val if l1 else 0
    #         y = l2.val if l2 else 0

    #         cur_val = x+y+carry
    #         carry = cur_val//10
    #         cur_val = cur_val%10
    #         cur_node = ListNode(cur_val)
    #         cur_node.next = l
    #         l = cur_node

    #         l1 = l1.next if l1 else None
    #         l2 = l2.next if l2 else None
                
    #     return l

    # 栈 头插法 (链表涉及到反转就要考虑到栈)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1)
            l1 = l1.next

        while l2:
            stack2.append(l2)
            l2 = l2.next

        ans = None
        carry = 0
        while stack1 or stack2 or carry:
            l1 = stack1.pop().val if stack1 else 0
            l2 = stack2.pop().val if stack2 else 0

            cur_val = l1+l2+carry
            carry = cur_val//10
            cur_val = cur_val%10
            cur_node = ListNode(cur_val)
            cur_node.next = ans
            ans = cur_node

        return ans

