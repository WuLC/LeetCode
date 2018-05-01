/*
 * Created on Tue May 01 2018 22:16:41
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// two pointers with hash map, O(n) time
class Solution 
{
    public:
        vector<int> findAnagrams(string s, string p) 
        {
            unordered_map<char, int> m;
            for(int i=0; i<p.size(); i++)
            {
                if (m.count(p[i]) > 0) m[p[i]]+=1;
                else m[p[i]] = 1;
            }
            
            unordered_map<char, int> tmp;
            vector<int> result;
            int left = 0, right = 0;
            while(right < s.size())
            {
                if (tmp.count(s[right]) > 0) tmp[s[right]]++;
                else tmp[s[right]] = 1;
                while(tmp[s[right]] > m[s[right]])
                {
                    tmp[s[left]]-=1;
                    left++;
                }
                if (right-left+1 == p.size()) 
                {
                    result.push_back(left);
                    tmp[s[left]]-=1;
                    left++;
                }
                right++;
            }
            return result;
        }
};