#encoding:utf-8
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


        


