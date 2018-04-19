/*
 * Created on Thu Apr 19 2018 14:24:27
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// change string in place with swap
class Solution 
{
    public:
        string reverseString(string s) 
        {
            for(int i = 0, j = s.size()-1; i<j; i++, j--)
                swap(s[i], s[j]);
            return s;
        }
};