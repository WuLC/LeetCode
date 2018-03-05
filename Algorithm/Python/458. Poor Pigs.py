# -*- coding: utf-8 -*-
# Created on Sun Jan 28 2018 15:19:45
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# referer: https://discuss.leetcode.com/topic/67666/another-explanation-and-solution
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        dim = minutesToTest / minutesToDie + 1
        while dim**pigs < buckets:
            pigs += 1
        return pigs
        