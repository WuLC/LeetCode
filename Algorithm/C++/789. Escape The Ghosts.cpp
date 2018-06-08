/*
 * Created on Fri Jun 08 2018 21:22:0
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// imagine the ghost just try to reach target as fast as possible
// if the ghost reach firstly, then you will never win
class Solution 
{
    public:
        bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) 
        {
            int dist = std::abs(target[0]) + std::abs(target[1]);
            for(auto g:ghosts)
            {
                if (std::abs(g[0]-target[0]) + std::abs(g[1]-target[1]) <= dist) return false;
            }
            return true;
        }
};