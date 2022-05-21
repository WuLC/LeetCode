#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        # check if loop exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                p1, p2 = head, fast
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None
            
# @lc code=end

