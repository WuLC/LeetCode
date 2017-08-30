# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-08-31 00:27:30
# @Last Modified by:   LC
# @Last Modified time: 2017-08-31 00:29:56


# simple rule
# referer: https://discuss.leetcode.com/topic/101113/c-java-clean-code-4-liner
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = []
        start, end = 1, n
        while k > 0:
            if (k & 1) == 1:
                result.append(start)
                start += 1
            else:
                result.append(end)
                end -= 1
            k -= 1
        result += [i for i in xrange(start, end+1)]
        return result