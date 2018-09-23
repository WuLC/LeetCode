# -*- coding: utf-8 -*-
# Created on Sun Sep 23 2018 11:2:27
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# binary search
class TopVotedCandidate(object):
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.result = []
        self.times = times
        count = {}
        curr_max  = 0
        for i in xrange(len(persons)):
            count.setdefault(persons[i], 0)
            count[persons[i]] += 1
            if count[persons[i]] >= curr_max:
                self.result.append(persons[i])
                curr_max = count[persons[i]]
            else:
                self.result.append(self.result[-1])

    def binary_search(self, t):
        if t >= self.times[-1]:
            return len(self.times)-1
        left, right = 0, len(self.times)-1
        while left < right:
            mid = left + ((right-left)>>1)
            if self.times[mid] == t:
                return mid
            elif self.times[mid] < t:
                left = mid + 1
            else:
                right = mid
        return left-1 if left>0 else 0

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        return self.result[self.binary_search(t)]