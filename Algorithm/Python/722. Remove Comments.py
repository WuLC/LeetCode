# -*- coding: utf-8 -*-
# Created on Fri Nov 17 2017 13:20:42
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# regular expression
import re
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        s = '\n'.join(source)
        return filter(lambda x:len(x)>0, re.sub('//.*|/\*(.|\n)*?\*/', '', s).split('\n'))
        
                    