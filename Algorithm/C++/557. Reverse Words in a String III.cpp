/*
 * Created on Thu Apr 19 2018 14:35:58
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// change string in place with swap
class Solution 
{
public:
    string reverseWords(string s) 
    {
        int curr = 0, p1, p2;
        while (curr < s.size())
        {
            p1 = curr;
            p2 = curr + 1;
            while (p2 < s.size() && s[p2] != ' ')
                p2++;
            curr = p2+1;
            p2--;
            while(p1 < p2)
            {
                swap(s[p1], s[p2]);
                p1++;
                p2--;
            }
        }
        return s;
    }
};