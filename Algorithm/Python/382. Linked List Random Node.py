# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-17 11:18:10
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-17 17:08:50
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


# reservoir sampling, O(1) space
# referer: https://discuss.leetcode.com/topic/53753/brief-explanation-for-reservoir-sampling, k = 1 is this problem 
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        tmp, num, count = self.head, None, 0
        while tmp:
            if random.randint(0,count) == 0:
                num = tmp.val
            count += 1
            tmp = tmp.next
        return num

