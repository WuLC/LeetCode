# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-27 01:58:03
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-27 01:58:16
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
        else:
            node = None