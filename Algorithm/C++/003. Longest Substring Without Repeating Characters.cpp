/*
 * Created on Sun Apr 15 2018 16:47:37
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// two pointers, O(n) time
// use hashmap to record indices
class Solution 
{
    public:
        int lengthOfLongestSubstring(string s)
        {
            unordered_map<char, int> idx;
            int curr = -1, result = 0;
            for(int i=0; i < s.length(); i++)
            {
                if (idx.find(s[i]) != idx.end()) curr = max(curr, idx[s[i]]);
                result = max(result, i-curr);
                idx[s[i]] = i;
            }
            return result;
        }
};