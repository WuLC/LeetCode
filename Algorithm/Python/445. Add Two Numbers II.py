# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-12-21 10:07:01
# @Last modified by:   WuLC
# @Last Modified time: 2016-12-21 13:03:34
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# method 1
# change linked-list directly to number, no overflow for python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None: return None
        num1, num2 = 0, 0
        while l1:
            num1 = num1*10 + int(l1.val)
            l1 = l1.next
        while l2:
            num2 = num2*10 + int(l2.val)
            l2 = l2.next
        dummy = ListNode(0)
        curr = dummy
        result = num1+num2
        for s in str(result):
            curr.next = ListNode(int(s))
            curr = curr.next
        return dummy.next

# method 2
# stack
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
        result, stack1, stack2 = [], [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carrier = 0
        # add two number
        while stack1 or stack2:
            tmp = carrier
            if stack1: 
                tmp += stack1.pop()
            if stack2: 
                tmp += stack2.pop()
            carrier, tmp = divmod(tmp, 10)
            result.append(tmp)
        if carrier == 1:
            result.append(carrier)
        # transfer number to linked list
        dummy = ListNode(0)
        curr = dummy
        while result:
            curr.next = ListNode(result.pop())
            curr = curr.next
        return dummy.next
        
            
            