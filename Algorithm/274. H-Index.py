# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-06-16 22:39:20
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-16 22:44:47
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        count = 0 
        citations.sort(reverse = True)
        for i in xrange(len(citations)):
            if count >= citations[i]:
                return count
            count += 1
        return count    # 0 element or 1 element 