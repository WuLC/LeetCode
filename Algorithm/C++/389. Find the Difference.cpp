/*
 * Created on Tue Jun 19 2018 19:40:56
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// hashmap
class Solution {
    public:
        char findTheDifference(string s, string t) 
        {
            std::map<char, int> count;
            for(char c:s)
                count[c] += 1;
            for(char c:t)
            {
                count[c] -= 1;
                if(count[c] < 0)
                    return c;
            }
        }
};