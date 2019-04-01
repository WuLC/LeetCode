# -*- coding: utf-8 -*-
# Created on Mon Apr 01 2019 22:50:31
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# stack, O(n) time, O(n) space

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        result, stack = [], []
        count, p = 0, head
        while p:
            result.append(0)
            while stack and stack[-1][1] < p.val:
                result[stack[-1][0]] = p.val
                stack.pop()
            stack.append((count, p.val))
            count += 1
            p = p.next
        return result


