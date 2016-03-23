# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 15:21:29 2016

@author: xhong
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(0)
        temp = result
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            carry, val = divmod(v1+v2+carry, 10)
            temp.next = ListNode(val)
            temp = temp.next
        return result.next

l1 = ListNode(0)
l1.next = ListNode(4)

l2 = ListNode(0)
l2.next = ListNode(5)

solution = Solution()
solution.addTwoNumbers(l1,l2)