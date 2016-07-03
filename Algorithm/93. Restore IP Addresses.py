# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-03 10:21:15
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-03 10:21:31
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n,result = len(s), []
        for a in xrange(1,4):
            for b in xrange(1,4):
                for c in xrange(1,4):
                    for d in xrange(1,4):
                        if a+b+c+d == n:
                            p1, p2, p3, p4 = s[:a],  s[a:a+b], s[a+b:a+b+c], s[a+b+c:]
                            if (p1.startswith('0') and len(p1) > 1) or \
                               (p2.startswith('0') and len(p2) > 1) or \
                               (p3.startswith('0') and len(p3) > 1) or \
                               (p4.startswith('0') and len(p4) > 1):
                               continue
                            if int(p1) <= 255 and int(p2) <= 255 and int(p3) <= 255 and int(p4) <= 255:
                                result.append('.'.join([p1,p2,p3,p4]))
        return result