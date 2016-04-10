# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-02-10 15:45:53
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:24:07
# @Email: liangchaowu5@gmail.com


#将数字转换为字符串再判断是否为回文

class Solution(object):
    def isPalindrome(self,x):
        """
        type x : int
        rtype :bool
        """
        strX=str(x)
        strLen=len(strX)
        flag=True
        for i in range(strLen/2):
            if strX[i] != strX[strLen-1-i]:
                flag=False
                return flag
        return flag