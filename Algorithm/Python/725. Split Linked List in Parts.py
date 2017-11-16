# -*- coding: utf-8 -*-
# Created on Thu Nov 16 2017 21:2:37
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# simple solution
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        curr = root
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        ave, remain = divmod(length, k)
    
        result = []
        curr, curr_head, tmp = root, None, None
        while curr:
            count = ave
            if remain > 0:
                count += 1
                remain -= 1
            curr_head = curr
            while count > 1:
                curr = curr.next
                count -= 1
            tmp = curr.next
            curr.next = None
            result.append(curr_head)
            curr =tmp
        while len(result) < k:
            result.append(None)
        return result
                
                
                
            