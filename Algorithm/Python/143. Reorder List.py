# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-05 09:45:18
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-05 09:45:28
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        nodes = collections.deque()
        while head:
            nodes.append(head)
            head = head.next
        tail = None
        while nodes:
            p1 = nodes.popleft()
            if head == None:
                head = p1
            p2 = nodes.pop() if nodes else None
            p1.next = p2 
            if tail != None:
                tail.next = p1
            tail = p2
        if tail:
            tail.next = None