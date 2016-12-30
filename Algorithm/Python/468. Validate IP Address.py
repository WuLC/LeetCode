# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-12-30 10:18:25
# @Last modified by:   WuLC
# @Last Modified time: 2016-12-30 10:19:39
# @Email: liangchaowu5@gmail.com


# split and then judge each part
# pay attention that in python all([]) will return True
class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        blocks = IP.split('.')
        if len(blocks) == 4:
            for block in blocks:
                if block and all([c.isdigit() for c in block]) and  0<= int(block) <=255 and (block.lstrip('0') == block or block == '0'):
                    continue
                else:
                    return 'Neither'
            return 'IPv4'
        blocks = IP.split(':')
        valid_chars = set('0123456789abcdefABCDEF')
        if len(blocks) == 8:
            for block in blocks:
                if block and len(block)<=4 and all([c in valid_chars for c in block]):
                    continue
                else:
                    return 'Neither'
            return 'IPv6'
        return 'Neither'
            
        