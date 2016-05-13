# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-13 08:58:02
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-13 08:58:27
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs = path.split('/')
        result = []
        for i in xrange(len(dirs)):
            if dirs[i] == '.' or dirs[i] == '':
                continue
            elif dirs[i] == '..':
                if len(result)>0:
                    result.pop()
            else:
                result.append(dirs[i])
        return '/'+'/'.join(result)