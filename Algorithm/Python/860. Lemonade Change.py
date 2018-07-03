# -*- coding: utf-8 -*-
# Created on Tue Jul 03 2018 12:33:47
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# hashmap, simple solution
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count = {5:0, 10:0, 20:0}
        for i in xrange(len(bills)):
            if bills[i] == 5:
                count[5] += 1
            elif bills[i] == 10:
                if count[5] == 0:
                    return False
                count[5] -= 1
                count[10] += 1
            elif bills[i] == 20:
                if count[10] > 0 and count[5] > 0:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False
        return True