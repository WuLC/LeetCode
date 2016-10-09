# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-27 23:09:22
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-28 15:23:47
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# method 1, hash table
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = set()
        while head:
            if head in nodes:
                return head
            nodes.add(head)
            head = head.next
        return None

# method 2 ,two pointers
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        p1, p2 = head, head
        while p1 and p2:
            if p1.next:
                p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                p1 = head
                while p1 and p2:
                    if p1 == p2:
                        return p1  
                    p1 = p1.next
                    p2 = p2.next
        return None