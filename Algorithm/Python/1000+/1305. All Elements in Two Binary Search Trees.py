# -*- coding: utf-8 -*-
# Created on Sun Jan 18 2020 10:23:32
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution 1, naive solution, get sorted value list for each tree
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        result = []
        stack1, stack2 = [], []
        curr1, curr2 = root1, root2
        while curr1 and curr1.left:
            stack1.append(curr1)
            curr1 = curr1.left
        while curr2 and curr2.left:
            stack2.append(curr2)
            curr2 = curr2.left
        while (curr1 or stack1) or (curr2 or stack2):
            if curr1 == None and stack1:
                curr1 = stack1.pop()
            if curr2 == None and stack2:
                curr2 = stack2.pop()
            if curr1 and curr2:
                if curr1.val < curr2.val:
                    result.append(curr1.val)
                    curr1 = curr1.right
                else:
                    result.append(curr2.val)
                    curr2 = curr2.right
            elif curr1:
                result.append(curr1.val)
                curr1 = curr1.right
            else:
                result.append(curr2.val)
                curr2 = curr2.right
        return result

# solution 2, in-order search with two binary search tree
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        result = []
        stack1, stack2 = [], []
        curr1, curr2 = root1, root2
        while curr1 and curr1.left:
            stack1.append(curr1)
            curr1 = curr1.left
        while curr2 and curr2.left:
            stack2.append(curr2)
            curr2 = curr2.left
        while (curr1 or stack1) or (curr2 or stack2):
            pop1, pop2 = False, False
            if curr1 == None and stack1:
                curr1 = stack1.pop()
            if curr2 == None and stack2:
                curr2 = stack2.pop()
            if curr1 and curr2:
                if curr1.val < curr2.val:
                    pop1 = True
                else:
                    pop2 = True
            elif curr1:
                pop1 = True
            else:
                pop2 = True
            if pop1:
                result.append(curr1.val)
                curr1 = curr1.right
                while curr1 and curr1.left:
                    stack1.append(curr1)
                    curr1 = curr1.left
            if pop2:
                result.append(curr2.val)
                curr2 = curr2.right
                while curr2 and curr2.left:
                    stack2.append(curr2)
                    curr2 = curr2.left
        return result

# make code of solution 2 more concise
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def reach_left_most(stack, node):
            while node and node.left:
                stack.append(node)
                node = node.left
            return node
        result, stack1, stack2 = [], [], []
        node1, node2 = root1, root2
        node1 = reach_left_most(stack1, node1)
        node2 = reach_left_most(stack2, node2)
        while (node1 or stack1) or (node2 or stack2):
            if node1 == None and stack1:
                node1 = stack1.pop()
            if node2 == None and stack2:
                node2 = stack2.pop()
            if (node1 and node2 and node1.val < node2.val) or (not node2):
                result.append(node1.val)
                node1 = reach_left_most(stack1, node1.right)
            else:
                result.append(node2.val)
                node2 = reach_left_most(stack2, node2.right)
        return result