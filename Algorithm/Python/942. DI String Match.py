# -*- coding: utf-8 -*-
# Created on Fri Nov 23 2018 21:6:11
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# greedy
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left, right = 0, len(S)
        result = []
        for i in xrange(len(S)):
            if S[i] == 'I':
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
        assert left == right, 'left not equal to right at the last element'
        result.append(left)
        return result