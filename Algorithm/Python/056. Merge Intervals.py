# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-07 09:18:47
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-07 09:20:30
# @Email: liangchaowu5@gmail.com

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# 先根据start排序，然后遍历，将在同一范围的merge
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x:x.start) # 根据interval的start从小到大排序
        result = []
        n = len(intervals)
        if n == 0:
            return result
        tmp = [intervals[0].start,intervals[0].end]
        for i in xrange(1,n):
            if tmp[0]<=intervals[i].start<=tmp[1]:
                if intervals[i].end>tmp[1]:
                    tmp[1] = intervals[i].end 
            else:
                result.append(Interval(tmp[0],tmp[1]))
                tmp = [intervals[i].start,intervals[i].end]
        result.append(Interval(tmp[0],tmp[1]))
        return result
        