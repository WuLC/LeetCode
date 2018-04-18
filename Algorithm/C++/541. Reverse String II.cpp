/*
 * Created on Thu Apr 19 2018 0:20:53
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// change the string in place with swap
class Solution 
{
    public:
        string reverseStr(string s, int k) 
        {
            for(int left=0; left < s.size(); left+=2*k)
            {
                for(int i = left, j = min(left+k-1, int(s.size())-1); i < j; i++, j--)
                    swap(s[i], s[j]);
            }
            return s;
        }
};

