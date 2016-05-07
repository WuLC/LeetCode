# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-07 20:19:41
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-07 20:34:38
# @Email: liangchaowu5@gmail.com

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        n = len(intervals)
        start = None
        end = None
        m1 = newInterval.start
        m2 = newInterval.end
        for i in xrange(n):
            if m1>intervals[i].end or m2 < intervals[i].start:
                result.append(intervals[i])
                continue
            if intervals[i].start<=m1<=intervals[i].end and start==None:
                start = intervals[i].start
            if intervals[i].start<=m2<=intervals[i].end and end==None:
                end = intervals[i].end
        if start == None:
            start = m1
        if end == None:
            end = m2
        result.append(Interval(start,end))
        result.sort(key=lambda x:x.start)
        return result

"""
最后三行代码也可换成下面的代码，不用对result排序，直接插入恰当的位置
        for i in xrange(len(result)):
        	if result[i].start > end:
        		result.insert(i,Interval(start,end))
        		return result
        result.append(Interval(start,end))
        return result
"""