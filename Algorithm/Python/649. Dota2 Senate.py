# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-08-08 19:48:52
# @Last Modified by:   WuLC
# @Last Modified time: 2017-08-08 19:53:44


# greedy, each senator ban its next opponent senator
from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r, d = deque(), deque()
        n = len(senate)
        for i in xrange(len(senate)):
            if senate[i] ==  'R':
                r.append(i)
            else:
                d.append(i)
            
        while len(r) > 0 and len(d) > 0:
            if r[0] > d[0]:
                d.append(d.popleft() + n)
                r.popleft()
            else:
                r.append(r.popleft() + n)
                d.popleft()
        return 'Radiant' if len(r) > 0 else 'Dire'
                    