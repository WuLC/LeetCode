# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-15 23:41:35
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-15 23:43:43
# @Email: liangchaowu5@gmail.com

# O(n) time 
# referer: https://discuss.leetcode.com/topic/79938/super-short-easy-java-o-n-solution

class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        n, total = len(machines), sum(machines)
        if total % n != 0:
            return -1
        ave = total/n
        diff = [machines[i]-ave for i in xrange(n)]
        result, tmp = 0, 0
        for i in xrange(n):
            tmp += diff[i]
            result = max(result, abs(tmp), diff[i])
        return result