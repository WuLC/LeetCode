# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-07 19:14:43
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-07 19:43:21
# @Email: liangchaowu5@gmail.com

# sort and DP
# O(n^2)，TLE
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key = lambda x:x[0])
        count = [1 for i in xrange(len(envelopes))]
        result = 0
        for i in xrange(len(envelopes)):
            for j in xrange(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    count[i] = max(count[i], count[j] + 1)
            result = max(count[i], result)
        return result


# sort and find longest increasing subsequence(the same as problem 300)
# O(nlgn), AC
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def compare(x,y):
            if x[0] != y[0]:
                return x[0] - y[0]
            else:
                return y[1] - x[1]
        envelopes.sort(cmp = compare)
        tails = []
        for env in envelopes:
            if len(tails) == 0 or env[1] > tails[-1]:
                tails.append(env[1])
            else:
                left, right = 0, len(tails)-1
                while left < right:
                    mid = left + (right - left)/2
                    if tails[mid] == env[1]:
                        break
                    elif tails[mid] > env[1]:
                        right = mid
                    else:
                        left = mid + 1
                if left >= right and tails[left] > env[1]:
                    tails[left] = env[1]
        return len(tails)