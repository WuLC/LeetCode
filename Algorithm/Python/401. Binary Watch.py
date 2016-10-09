# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-20 00:11:26
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-20 00:12:27
# @Email: liangchaowu5@gmail.com

# backtracking, bit manipulation
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num > 8:
            return []
        result = []
        for h in xrange(num+1):
            if h == 4: break
            if num - h > 6: continue
            hours, minutes = [], []
            self.get_hour(h, 0, 0, hours)
            self.get_miniute(num - h, 0, 0, minutes)
            for hour in hours:
                for miniute in minutes:
                    result.append(str(hour)+':'+str(miniute).zfill(2))
        return result
        
    def get_hour(self,  n, idx, tmp, result):
        if n == 0:
            result.append(tmp)
            return 
        for i in xrange(idx, 4):
            if tmp ^ (1<<i) > 11:
                return 
            else:
                self.get_hour(n-1, i+1, tmp^(1<<i), result)
                    
            
    def get_miniute(self, n, idx, tmp, result):
        if n == 0:
            result.append(tmp)
            return 
        for i in xrange(idx, 6):
            if tmp ^ (1<<i) > 59:
                return 
            else:
                self.get_miniute(n-1, i+1, tmp^(1<<i), result)
            
    