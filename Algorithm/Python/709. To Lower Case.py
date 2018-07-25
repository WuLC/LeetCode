# -*- coding: utf-8 -*-
# Created on Wed Jul 25 2018 9:56:18
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# change with ascii code
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return ''.join([chr(ord(c)+32) if  65<=ord(c)<=90 else c for c in str])