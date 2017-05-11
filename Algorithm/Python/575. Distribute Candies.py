# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-05-11 18:01:34
# @Last modified by:   WuLC
# @Last Modified time: 2017-05-11 18:02:12
# @Email: liangchaowu5@gmail.com


# count the number of different kinds of candies
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        count = 0
        record = set()
        for candy in candies:
            if candy not in record:
                count += 1
                record.add(candy)
            if count >= (len(candies)>>1):
                break
        return count
        