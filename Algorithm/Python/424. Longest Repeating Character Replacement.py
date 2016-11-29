# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-28 23:42:52
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-29 00:06:10
# @Email: liangchaowu5@gmail.com

# two pointers 
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = 0
        if len(s) == 0:
            return result
        left, right = 0, 0
        count = collections.defaultdict(int)
        while right < len(s):
            count[s[right]] += 1
            curr_max = max(count.values())
            while right - left - curr_max + 1 > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
            right += 1
        return result
        

# use array to save space since all characters are capital 
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = 0
        if len(s) == 0:
            return result
        left, right = 0, 0
        count = [0 for i in xrange(26)]
        while right < len(s):
            count[ord(s[right])-65] += 1
            curr_max = max(count)
            while right - left - curr_max + 1 > k:
                count[ord(s[left])-65] -= 1
                left += 1
            result = max(result, right - left + 1)
            right += 1
        return result