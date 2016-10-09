# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-13 19:21:56
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-13 19:23:54
# @Email: liangchaowu5@gmail.com

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.original = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        return random.sample(self.original, len(self.original))
        """
        tmp = self.original[:]
        n = len(tmp)-1
        while n > 0:
            idx = random.randint(0, n)
            tmp[idx], tmp[n] = tmp[n], tmp[idx]
            n -= 1
        return tmp
        """