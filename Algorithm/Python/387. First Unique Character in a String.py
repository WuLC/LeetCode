# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-07 17:17:14
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-07 17:17:20
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        index, repeat = {}, set()
        for i in xrange(len(s)):
            if s[i] in repeat:
                continue
            elif s[i] in index:
                del index[s[i]]
                repeat.add(s[i])
            else:
                index[s[i]] = i
        unrepeat = sorted(index.items(), key = lambda x:x[1])
        return unrepeat[0][1] if unrepeat else -1