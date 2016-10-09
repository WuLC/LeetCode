# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-27 22:53:16
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-27 22:53:27
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull, cow = 0, 0
        sec_dic, gue_dic = {}, {}
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if secret[i] not in sec_dic:
                    sec_dic[secret[i]] = 0
                sec_dic[secret[i]] += 1
                if guess[i] not in gue_dic:
                    gue_dic[guess[i]] = 0
                gue_dic[guess[i]] += 1
        for k,v in sec_dic.items():
            if k in gue_dic:
                cow += gue_dic[k] if gue_dic[k] < sec_dic[k] else sec_dic[k]
        return "%sA%sB"%(bull,cow)
                