# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-26 23:50:56
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-26 23:51:02
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left, right, n, h_index = 0, len(citations)-1, len(citations), 0
        while left <= right:
            mid = (left + right)/2
            count = n-mid
            if count == citations[mid]:
                return count
            elif count < citations[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return n-left