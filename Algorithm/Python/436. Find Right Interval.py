# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-11-10 20:54:45
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-10 20:55:10
# @Email: liangchaowu5@gmail.com

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e



# hashtable and binary search
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        start_indices = {}
        for i in xrange(len(intervals)):
            start_indices[intervals[i].start] = i
        starts = sorted(start_indices.keys())
        result = []
        
        for inter in intervals:
            if inter.end in start_indices:
                result.append(start_indices[inter.end])
            elif inter.end >= starts[-1]:
                result.append(-1)
            else:
                left, right = 0, len(starts) - 1
                while left < right:
                    mid = left + ((right-left)>>1)
                    if starts[mid] > inter.end:
                        right = mid
                    else:
                        left = mid + 1
                result.append(start_indices[starts[left]])
        return result