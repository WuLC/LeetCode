# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-17 11:18:10
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-17 11:19:04
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# O(n) space
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.values = []
        self.n = 0
        while head:
            self.values.append(head.val)
            head = head.next
            self.n += 1

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        return self.values[random.randint(0, self.n -1)]