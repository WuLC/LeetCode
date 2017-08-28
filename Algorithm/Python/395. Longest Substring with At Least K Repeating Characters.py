# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-18 23:51:04
# @Last modified by:   WuLC
# @Last Modified time: 2017-08-26 11:26:25
# @Email: liangchaowu5@gmail.com

# O(n^2) time, TLE
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = 0
        for i in xrange(len(s)):
            count, not_enough = {}, set()
            for j in xrange(i, len(s)):
                count.setdefault(s[j], 0)
                count[s[j]] += 1
                if count[s[j]] < k:
                    not_enough.add(s[j])
                else:
                    not_enough.discard(s[j])
                    if len(not_enough) == 0:
                        result = max(result, j-i+1)
        return result


# split the string by the characters whoses apprearing times is less than k
# in terms of Master's theorem, O(nlgn) time, AC
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for char in set(s):
            if s.count(char) < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
        return len(s)