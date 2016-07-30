# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-30 11:00:18
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-30 11:14:28
# @Email: liangchaowu5@gmail.com


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# method 1,directly implement insertion sort on the linked list,O(n^2),TLE
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        p1 = head.next
        dummy = ListNode(0)
        dummy.next, end, end.next = head, head, None
        while p1:
            p2 = p1.next
            tmp1, tmp2 = dummy, dummy.next
            while tmp2:
                if p1.val < tmp2.val:
                    tmp1.next = p1
                    p1.next = tmp2
                    break
                else:
                    tmp1 = tmp1.next
                    tmp2= tmp2.next
            if tmp2 == None:
                end.next = p1
                end = end.next
                end.next = None
            p1 = p2
        return dummy.next
        
        
# method 2, copy the values of the linked list to an array and sort the array, O(nlogn), AC
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp,values = head, []
        while tmp:
            values.append(tmp.val)
            tmp = tmp.next
        tmp = head
        values.sort()
        for i in xrange(len(values)):
            tmp.val = values[i]
            tmp = tmp.next
        return head
            