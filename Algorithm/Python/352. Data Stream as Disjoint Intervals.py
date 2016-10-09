# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-22 15:12:24
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-22 22:19:47
# @Email: liangchaowu5@gmail.com


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e



# the final result has to be in order 


# method 1, modify the intervals directly and sort the result
class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inter = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        idx, merge_2 = None, False
        for i in xrange(len(self.inter)):
            if self.inter[i].start <= val <=self.inter[i].end:
                return
            if self.inter[i].start - val == 1:
                if idx == None:
                    self.inter[i].start = val
                    idx = i
                else:
                    self.inter[idx].end = self.inter[i].end
                    idx = i
                    merge_2 = True
                    break
            elif self.inter[i].end - val == -1:
                if idx == None:
                    self.inter[i].end = val
                    idx = i
                else:
                    self.inter[idx].start = self.inter[i].start
                    idx = i
                    merge_2 = True
                    break
        if idx == None:
            self.inter.append(Interval(s=val, e=val))
        if merge_2:
            self.inter.remove(self.inter[i])
             
    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return sorted(self.inter, key = lambda x:x.start)


