# -*- coding: utf-8 -*-
# Created on Sun Jul 29 2018 22:15:0
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# simple solution
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        count = count//2
        curr = head
        while count > 0:
            curr = curr.next
            count -= 1
        return curr