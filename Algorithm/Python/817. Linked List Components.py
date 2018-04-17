# -*- coding: utf-8 -*-
# Created on Tue Apr 17 2018 9:18:48
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# two pointers
# connected nodes as a component
class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        count = 0
        G = set(G)
        p1, p2 = head, head
        while p2:
            while p2 and p2.val in G:
                p2 = p2.next
            if p1 != p2:
                count += 1
            if p2:
                p2 = p2.next
                p1 = p2
        return count