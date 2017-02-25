# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-25 20:12:39
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-25 20:14:51
# @Email: liangchaowu5@gmail.com


# one line solution, use `all` and generator
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return all((c.islower() for c in word[1:])) or all((c.isupper() for c in word))