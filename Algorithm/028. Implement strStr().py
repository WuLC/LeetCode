class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0: 
            return -1
            
        hlen = len(haystack)
        nlen = len(needle)
        for i in range(hlen-nlen+1):
            if haystack[i:i+nlen] == needle:
                return i
        return -1
            
            
            
            
            