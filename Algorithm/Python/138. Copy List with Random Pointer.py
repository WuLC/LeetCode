# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-21 08:34:39
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-21 09:44:28
# @Email: liangchaowu5@gmail.com


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# can't modify the original linkedlist 

# method 1, O(n^2) time complexity, O(1) space, TLE
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dummy = RandomListNode(0)
        p1, p2, count = dummy, head, 0
        while p2:
            p1.next = RandomListNode(p2.label)
            p1 = p1.next
            p2 = p2.next
            count += 1
        p1 = dummy.next
        while head:
            p2 = head.random
            length = 0
            while p2:
                p2 = p2.next
                length += 1
            dis = count - length
            tmp = dummy.next
            for i in xrange(dis):
                tmp = tmp.next
            p1.random = tmp
            p1 = p1.next
            head = head.next
        return dummy.next

# method 2, O(n) time complexity, O(n) space, AC
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        nodes, node = {}, head
        while node:
            nodes[node] = RandomListNode(node.label)
            node = node.next
        node, start = head, None
        while node:
            if start == None:
                start = nodes[node]
            nodes[node].next = nodes.get(node.next, None)
            nodes[node].random = nodes.get(node.random, None)
            node = node.next
        return start


# method 3, O(n) time xomplexity, O(1) space, AC
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # duplicate all nodes
        node = head
        while node:
            tmp = node.next
            dup = RandomListNode(node.label)
            node.next = dup
            dup.next = tmp
            node = tmp
        node = head
        # set random for new nodes
        while node:
            node.next.random = node.random.next if node.random else None
            node = node.next.next
        # extract new nodes from linkedlist
        node, start, curr = head, None, None
        while node:
            if start == None:
                start = node.next
                curr = node.next
            else:
                curr.next = node.next
                curr = curr.next
            node.next = node.next.next
            node = node.next
        return start