# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-03-13 09:19:13
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:24:49
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(n,n,'',res)
        return res
        
    def  helper(self,left,right,item,res):
        if left==0 and right==0:
            res.append(item)
            return
        if left>0:
            self.helper(left-1,right,item+'(',res)
        if right>left:
            self.helper(left,right-1,item+')',res)


        


