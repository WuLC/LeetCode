# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-09 14:12:14
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-09 14:21:33
# @Email: liangchaowu5@gmail.com

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peak = self.iterator.next() if self.iterator.hasNext() else  None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.peak
        

    def next(self):
        """
        :rtype: int
        """
        tmp = self.peak
        self.peak = self.iterator.next() if self.iterator.hasNext() else  None
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peak != None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].