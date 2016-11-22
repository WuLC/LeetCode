# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-22 17:01:37
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-22 17:06:26
# @Email: liangchaowu5@gmail.com


# math
# referer: https://discuss.leetcode.com/topic/38014/java-oms-with-explanation
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        for i in xrange(3, len(x)):
            if i==3 and x[i]>=x[i-2] and x[i-1]<=x[i-3]:
                return True
            elif i==4 and x[i-1]==x[i-3] and x[i] + x[i-4] == x[i-2]:
                return True
            elif i>=5 and x[i-2] >= x[i-4] and x[i-4] + x[i] >= x[i-2] and x[i-1] <= x[i-3] and x[i-5] + x[i-1] >= x[i-3]:
                return True
        return False