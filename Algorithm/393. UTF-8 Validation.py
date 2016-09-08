# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-08 23:08:58
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-08 23:09:54
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        index = 0
        while index < len(data):
            bin_num = '{0:08b}'.format(data[index]) # format the number to a eight-bit bianry string
            if bin_num[0] == '0':
                index += 1
                continue
            count, inx = 0, 0
            while bin_num[inx] == '1':
                count += 1
                if count > 4: 
                    return False
                inx += 1
            
            if count == 1 or index + count - 1 >= len(data):
                return False
            for i in xrange(index+1, index+count):
                if '{0:08b}'.format(data[i]).startswith('10'):
                    continue
                else:
                    return False
            index += count
        return True