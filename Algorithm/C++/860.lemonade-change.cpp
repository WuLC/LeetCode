/*
 * @lc app=leetcode id=860 lang=cpp
 *
 * [860] Lemonade Change
 */

// @lc code=start
#include<vector>
#include<unordered_map>

class Solution {
public:
    bool lemonadeChange(std::vector<int>& bills) {
        std::unordered_map<int, int> remains{{5,0}, {10,0}, {20,0}};
        std::vector<int> candidates{10, 5};
        int change = 0;
        for(auto b: bills) {
            remains[b]++;
            change = b - 5;
            for(int cand : candidates) {
                while(change > 0 && change >= cand && remains[cand] > 0) {
                    change -= cand;
                    remains[cand]--;
                }
            }
            if (change > 0) return false;
        }
        return true;
    }
};
// @lc code=end

