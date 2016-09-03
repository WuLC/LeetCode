# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-03-10 18:09:28
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-03 20:58:47
# @Email: liangchaowu5@gmail.com

# backtracking 
class Solution(object):
    numDict ={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        self.helper(0, digits, '', result)
        return result
    
    def helper(self, index, digits, tmp, result):
        if index == len(digits):
            if tmp: # empty string
                result.append(tmp)
            return
        for char in Solution.numDict[digits[index]]:
            self.helper(index+1, digits, tmp+char, result)


# combine a new letter with previous results
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        numDict ={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        result = []
        if len(digits)==0:
            return result
        # 先将第一位对应的字符复制给result，防止调用函数combine2StrList时一开始result为空
        result = numDict[digits[0]]   
        for i in range(1,len(digits)):
            result = self.combine2StrList(result,numDict[digits[i]])
        return result
            
    
    def combine2StrList(self,s1,s2):
        mix =[]
        for i in range(len(s1)):
            for j in range(len(s2)):
               mix.append(s1[i]+s2[j])
        return mix
