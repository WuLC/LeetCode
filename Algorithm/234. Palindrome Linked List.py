# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-27 09:22:13
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-28 17:56:12
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# method 1, O(n) time, O(n) space
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

# method 2, O(n) time, O(1) space
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        tmp, count = head, 0
        while tmp:
            count += 1
            tmp = tmp.next
        mid = count/2 if count % 2==1 else count/2-1
        tmp = head
        for i in xrange(mid):
            tmp = tmp.next
        tmp.next = self.reverse_list(tmp.next)
        p1, p2 = head, tmp.next
        is_palindrome = True
        while p2:
            if p1.val != p2.val:
                is_palindrome = False
                break
            p1, p2 = p1.next, p2.next
        tmp.next = self.reverse_list(tmp.next)
        return is_palindrome
        
            
    def reverse_list(self, head):
        dummy = ListNode(0)
        dummy.next = head
        p1, p2 = dummy, dummy.next
        while p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        if dummy.next:
            dummy.next.next = None
            dummy.next = p1
        return dummy.next