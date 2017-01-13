# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-01-13 15:16:40
# @Last modified by:   WuLC
# @Last Modified time: 2017-01-13 15:28:38
# @Email: liangchaowu5@gmail.com


# method 1, naive solution, build the magical string and count the number of '1' one by one
# very slow
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        magical_string = '122'
        idx, count, total = 0, 0, 0
        while total+int(magical_string[idx]) < n:
            total += int(magical_string[idx])
            char = '1' if idx%2==0 else '2'
            if idx > 1:
                magical_string += char*int(magical_string[idx])
            if char == '1':
                count += int(magical_string[idx])
            idx += 1
        if idx%2 == 0:
            count += (n-total) # final left number
        return count


# fast solution
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        S = [1,2,2]
        idx = 2
        while len(S) < n:
            S += S[idx] * [(3 - S[-1])]
            idx += 1
        return S[:n].count(1)