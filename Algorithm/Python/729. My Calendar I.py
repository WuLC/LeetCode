# -*- coding: utf-8 -*-
# Created on Mon Dec 04 2017 22:56:48
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# method 1
# binary search with array
# time complexity: bianry search O(logn), insertion O(n)
class MyCalendar(object):

    def __init__(self):
        self.record = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.record) == 0:
            self.record.append((start, end))
            return True
        left, right = 0, len(self.record) - 1
        while left < right:
            mid = left + ((right-left)>>1)
            if self.record[mid][0] >= end:
                right = mid - 1
            elif self.record[mid][1] <= start:
                left = mid + 1
            else:
                return False
            
        if self.record[left][0]>=end:
            self.record.insert(left,(start, end))
            return True
        elif self.record[left][1]<=start:
            self.record.insert(left + 1 , (start, end))
            return True
        else:
            return False
            

# method 2
# binary search with binary search tree
# time complexity: bianry search O(logn), insertion O(1)

class Node():
    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.left = None
        self.right = None

class MyCalendar(object):
    def __init__(self):
        self.root = Node(0,0)
    
    def insert(self, start, end, node):
        if start >= node.end:
            if node.right:
                return self.insert(start, end, node.right)
            else:
                node.right = Node(start, end)
                return True
        elif end <= node.start:
            if node.left:
                return self.insert(start, end, node.left)
            else:
                node.left = Node(start, end)
                return True
        else:
            return False
        
    def book(self, start, end):
        return self.insert(start, end, self.root)