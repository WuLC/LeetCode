# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-03-12 09:43:41
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:24:40
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 15.94%
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        dummy = ListNode(0)
        nextNode = dummy
        while l1 and l2:
            if l1.val > l2.val:
                nextNode.next = l2
                nextNode = nextNode.next
                l2 = l2.next
            else:
                nextNode.next = l1
                nextNode = nextNode.next
                l1 = l1.next
        
        if l1:
            nextNode.next = l1
            
        if l2:
            nextNode.next = l2
        
        return dummy.next
                