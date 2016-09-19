# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-19 16:52:38
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-19 16:53:21
# @Email: liangchaowu5@gmail.com

# divide and conquer
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        result = []
        for i in xrange(len(input)):
            if input[i] in {'+','-','*'}:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for num1 in left:
                    for num2 in right:
                        if input[i] == '+':
                            result.append(num1+num2)
                        elif input[i] == '-':
                            result.append(num1-num2)
                        else:
                            result.append(num1*num2)
        # deal with str thar only contains digits
        if input and len(result) == 0:
            result.append(int(input))
        return result