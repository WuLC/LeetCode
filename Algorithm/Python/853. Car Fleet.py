# -*- coding: utf-8 -*-
# Created on Sun Jun 17 2018 15:4:38
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# calculate the time required for each car in the order of their positions
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pos = sorted(list(zip(position, speed)))
        time = [(target-p[0])*1.0/p[1] for p in pos]
        count = 0
        idx = len(time)-1
        for i in reversed(xrange(len(time)-1)):
            if time[i] > time[idx]:
                count += 1
                idx = i
        if len(time) > 0:
            count += 1
        return count