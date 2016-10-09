# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-20 09:44:41
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-20 09:50:45
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# two pointers,point to closest different values
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        p1, p2= head, head.next
        while p2 :
            if p2.val != p1.val:
                if p1.next == p2:
                    if dummy.next == None:
                        curr = p1
                        dummy.next = curr
                    else:
                        curr.next = p1
                        curr = curr.next
                p1 = p2
            p2 = p2.next
            
        if p1.next == None:        # the last element is valid
            if dummy.next == None: # only the last element is valid in the list 
                dummy.next = p1
            else:
                curr.next = p1
        else:                   
            if dummy.next != None:
                curr.next = None
        return dummy.next       
        