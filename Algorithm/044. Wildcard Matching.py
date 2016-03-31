#encoding:utf-8
#方案一:递归，超时
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0:
            if len(p) == 0 or (p[0] == '*' and p== p[0]*len(p)):
                return True
            else:
                return False
            
        if len(p) == 0:
            if len(s) == 0:
                return True
            else:
                return False
        i = 0
        j = 0
        
        if p[j] == '?':
            return self.isMatch(s[i+1:],p[j+1:])
        elif p[j] == '*':
            for i in range(len(s)+1):
                if self.isMatch(s[i:],p[j+1:]):
                    return True
            return False
        else:
            return s[i]==p[j] and self.isMatch(s[i+1:],p[j+1:])
 

# 方案二：双指针回溯
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p_index, s_index, last_s_index, last_p_index = 0, 0, -1, -1
        while s_index < len(s):
            # Normal match including '?'
            if p_index < len(p) and (s[s_index] == p[p_index] or p[p_index] == '?'):
                s_index += 1
                p_index += 1
            # Match with '*'
            elif p_index < len(p) and p[p_index] == '*':
                p_index += 1
                last_s_index = s_index
                last_p_index = p_index
            # Not match, but there is a '*' before
            elif last_p_index != -1:
                last_s_index += 1
                s_index = last_s_index
                p_index = last_p_index
            # Not match and there is no '*' before
            else:
                return False
        # Check if there is still character except '*' in the pattern
        while p_index < len(p) and p[p_index] == '*':
            p_index += 1
        # If finish scanning both string and pattern, then it matches well
        return p_index == len(p)



'''
测试递归方法，，虽然答案正确，但是超时       
if __name__ == '__main__':
    s = Solution()
    print s.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab","***bba**a*bbba**aab**b")
'''