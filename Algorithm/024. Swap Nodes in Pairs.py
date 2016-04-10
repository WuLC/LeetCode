# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-03-29 10:05:03
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:23:26
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next ==None:
            return head
        
        front = head
        lastend = front
        back = head.next
        tmp = back.next
        dummy = ListNode(0)
        dummy.next = back

        while front and back:
            back.next = front
            lastend.next = back # 连接前面已经swap了的nodes和本次swap的node
            front.next = tmp
            lastend = front   # 记录上一次调换后的最后一个node
            front = front.next
            if front:
                back = front.next
                if back:
                    tmp = back.next
                else:
                    break
            else:
                break
           
        return dummy.next
                
        