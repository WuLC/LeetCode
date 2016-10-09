# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-10-09 15:12:03
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-09 15:34:13
# @Email: liangchaowu5@gmail.com


# split the number, from tail to head, three digits as a group
# then translate each group with helper function dealing with those rules
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        map1 = {'0':'Zero', '1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine','10':'Ten', '11':'Eleven', '12':'Twelve', '13':'Thirteen', '14': 'Fourteen', '15':'Fifteen' , '16':'Sixteen', '17':'Seventeen', '18':'Eighteen', '19':'Nineteen'}
        map2 = {'2':'Twenty', '3':'Thirty', '4':'Forty', '5':'Fifty', '6':'Sixty', '7':'Seventy', '8':'Eighty', '9':'Ninety'}
        def helper(s):
            if len(s) == 1:
                return map1[s]
            elif len(s) == 2:
                if s[0] == '1':
                    return map1[s] 
                else:
                    return map2[s[0]] if s[1] == '0' else map2[s[0]]+' '+map1[s[1]]
            elif len(s) == 3:
                tmp = ''
                if s[0] != '0':
                    tmp = map1[s[0]] +' Hundred'
                if s[1] != '0':
                    if s[1] == '1':
                        tmp += ' '+map1[s[1:]] if tmp else map1[s[1:]]
                        return tmp
                    else:
                        tmp += ' '+map2[s[1]] if tmp else map2[s[1]]
                if s[2] != '0':
                    tmp += ' '+map1[s[2]] if tmp else map1[s[2]]
                return tmp
            
        # split the number 
        s = str(num)
        idx, groups = len(s), []
        while idx > 0:
            if idx - 3 >= 0:
                groups.append(s[idx-3:idx])
            else:
                groups.append(s[:idx])
            idx -= 3
        
        result = ''
        suffix = {1:' Thousand', 2:' Million', 3:' Billion'}
        for i in xrange(len(groups)):
            tmp = helper(groups[i])
            if tmp:
                if i != 0:
                    tmp += suffix[i]
                result = tmp + ' ' + result
        return result.strip()

            