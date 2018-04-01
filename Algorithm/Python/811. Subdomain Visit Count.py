# -*- coding: utf-8 -*-
# Created on Sun Apr 01 2018 11:11:31
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# hashmap, simple counting
from collections import defaultdict
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        count = defaultdict(int)
        for cpd in cpdomains:
            num, domain = cpd.split()
            num = int(num)
            ds = domain.split('.')
            for i in reversed(xrange(len(ds))):
                count['.'.join(ds[i:])] += num
        result = []
        for k, v in count.items():
            result.append('{0} {1}'.format(v, k))
        return result
        