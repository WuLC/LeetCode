# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-17 15:20:10
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-17 15:23:40
# @Email: liangchaowu5@gmail.com


# use the method to transform number from base 10 to any base 
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        flag = 1
        if num < 0:
            flag = -1
            num = -num
        result = ''
        while num:
            num, bit = divmod(num, 7)
            result = str(bit) + result
        if flag == -1:
            result = '-'+result
        return result