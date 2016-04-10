# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-01-23 10:53:34
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:23:45
# @Email: liangchaowu5@gmail.com


#########################################
# 注意：
# 题目已经定义好了链表类
# 链表的相加进位
###########################################


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(0)
        tmp=head
        flag=0
        while l1 or l2:
            sum=flag
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            if sum>=10:
                qua=sum%10
                flag=1
                tmp.next=ListNode(qua)
                tmp=tmp.next
            else:
                flag=0
                tmp.next=ListNode(sum)
                tmp=tmp.next
        if flag==1:
            tmp.next=ListNode(1)
        return head.next
        