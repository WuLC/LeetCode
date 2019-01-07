# -*- coding: utf-8 -*-
# Created on Sun Jan 06 2019 21:3:59
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# get candidates for x**i and y**j and add them up
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        candidate_x, i = [1], 1
        if x != 1:
            tmp = x**i
            while tmp < bound:
                candidate_x.append(tmp)
                i += 1
                tmp = x**i

        candidate_y, j = [1], 1
        if y != 1:
            tmp = y**j
            while tmp < bound:
                candidate_y.append(tmp)
                j += 1
                tmp = y**j
        
        result = set()
        for i in xrange(len(candidate_x)):
            for j in xrange(len(candidate_y)):
                if candidate_x[i] + candidate_y[j] > bound:
                    break
                result.add(candidate_x[i] + candidate_y[j])
        return list(result)
                    