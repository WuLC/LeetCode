# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-06-17 10:26:14
# @Last modified by:   LC
# @Last Modified time: 2017-06-17 10:50:32
# @Email: liangchaowu5@gmail.com

# 1. seperate all numerators and denominators and store them seperately in a list 
# 2. find lcm(lowest common multiple) for all denominators 
# 3. calculate sum of numerator in terms of lcm
# 4. find gcd(greatest common divisor) for final numerator and denominator

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # re can split string with multiple delimeter
        # import re
        # nums = re.split('[+-]', expression)
        s = '+' + expression if expression[0] != '-' else expression
        sign = [i for i in xrange(len(s)) if s[i] in ('+', '-')]
        sign.append(len(s))
        
        numerator, denominator = [], []
        for i in xrange( len(sign) - 1 ):
            n, d = s[sign[i] + 1:sign[i+1]].split('/')
            flag = -1 if s[sign[i]] == '-' else 1
            numerator.append(int(n) * flag)
            denominator.append(int(d))
        
        def gcd(n1, n2):
            if n1 < n2:
                n1, n2 = n2, n1
            while n2 != 0:
                n1, n2 = n2, n1 % n2
            return n1
            
        lcm = reduce(lambda a,b: a*b/gcd(a,b), denominator)
        numerator_sum = 0
        for i in xrange(len(numerator)):
            numerator_sum += numerator[i] * (lcm / denominator[i])
        # gcd for numerator and denominator
        commom = gcd(abs(numerator_sum), lcm)
        return str(numerator_sum/commom) + '/' + str(lcm/commom)
        