/*
 * Created on Tue May 08 2018 22:17:59
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// simple solution, not necessary to use all characters
class Solution 
{
    public:
        int longestPalindrome(string s)
        {
            unordered_map<char, int> counter;
            for(char c : s)
            {
                if (counter.count(c) > 0) counter[c]++;
                else counter[c] = 1;
            }
            int result = 0;
            bool odd = false;
            for(auto it=counter.begin(); it!=counter.end(); it++)
            {
                if((it->second & 1)) 
                {
                    result += it->second - 1;
                    odd = true;
                }
                else result += it->second;
            }
            return odd ? result+1 : result;
        }
};