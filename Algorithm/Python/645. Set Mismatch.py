# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-07-24 08:32:19
# @Last modified by:   LC
# @Last Modified time: 2017-07-24 08:32:36
# @Email: liangchaowu5@gmail.com


# use set
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = set(range(1, len(nums)+1))
        result = []
        for num in nums:
            if num in tmp:
                tmp.remove(num)
            else:
                result.append(num)
        result.append(list(tmp)[0])
        return result