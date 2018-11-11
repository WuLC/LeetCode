# -*- coding: utf-8 -*-
# Created on Sun Nov 11 2018 10:44:36
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# custom key for sorting
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digital_logs, letter_logs  = [], []
        for log in logs:
            if log[-1].isdigit():
                digital_logs.append(log)
            else:
                letter_logs.append(log)        
        return sorted(letter_logs, key = lambda s : ' '.join(s.split()[1:])) + digital_logs
        
