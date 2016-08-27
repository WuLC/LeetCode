# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-27 09:22:13
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-27 09:23:38
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# O(n) time, O(n) space
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []
        p = head
        while p:
            values.append(p.val)
            p = p.next
        left, right = 0, len(values)-1
        while left < right:
            if values[left]!=values[right]:
                return False
            left += 1
            right -= 1
        return True

# O(n) time, O(1) space
