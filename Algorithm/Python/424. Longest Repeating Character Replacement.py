# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-28 23:42:52
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-28 23:51:59
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
        
        