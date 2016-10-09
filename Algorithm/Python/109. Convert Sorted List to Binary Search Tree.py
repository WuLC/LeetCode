# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-30 19:30:53
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-30 19:31:13
# @Email: liangchaowu5@gmail.com


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.helper(0, len(nums)-1, nums)
        
    def helper(self, left, right, nums):
        if left > right:
            return
        if left == right:
            return TreeNode(nums[left])
        mid = (left+right)/2
        root = TreeNode(nums[mid])
        left = self.helper(left, mid-1, nums)
        right = self.helper(mid+1, right, nums)
        root.left, root.right = left, right
        return root
            