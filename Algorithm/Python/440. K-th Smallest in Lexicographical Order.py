# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-21 22:04:38
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-21 22:10:14
# @Email: liangchaowu5@gmail.com

# referer: https://discuss.leetcode.com/topic/64462/c-python-0ms-o-log-n-2-time-o-1-space-super-easy-solution-with-detailed-explanations
# general idea: 
# 1) count the total number of numbers that start with certain digits
# 2) change the prefix digits according to the value of k and the counting result,repeat process 1) till k is 1
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        result = 1
        while k > 1:
            count = 0
            interval = [result, result+1]
            while interval[0] <= n:
                count += min(n+1, interval[1]) - interval[0]
                interval = [interval[0]*10, interval[1]*10]
            if k > count:
                k -= count
                result += 1
            else:
                k -= 1
                result *= 10
        return result