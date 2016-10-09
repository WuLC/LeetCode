# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-10 23:06:39
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-10 23:07:10
# @Email: liangchaowu5@gmail.com

from fractions import gcd
class Solution(object):
    def canMeasureWater(self, x, y, z):
        return z == 0 or x + y >= z and z % gcd(x, y) == 0