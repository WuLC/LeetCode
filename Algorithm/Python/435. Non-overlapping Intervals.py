# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-09 12:51:58
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-09 12:55:15
# @Email: liangchaowu5@gmail.com

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# greedy
# Which interval would be the best first (leftmost) interval to keep?
# One that ends first, as it leaves the most room for the rest.
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        count = 0
        curr_end = None
        for inter in sorted(intervals, key = lambda x:x.start):
            if curr_end == None:
                curr_end = inter.end
                continue
            if inter.start < curr_end:
                count += 1
                curr_end = min(inter.end, curr_end)
            else:
                curr_end = inter.end
        return count 

# referer solution
def eraseOverlapIntervals(self, intervals):
    end = float('-inf')
    erased = 0
    for i in sorted(intervals, key=lambda i: i.end):
        if i.start >= end:
            end = i.end
        else:
            erased += 1
    return erased