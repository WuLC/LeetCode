/*
 * @lc app=leetcode id=1540 lang=cpp
 *
 * [1540] Can Convert String in K Moves
 */

// @lc code=start

#include <string>
#include <vector>
#include <unordered_set>


// use fixed-len counter instead of set to avoid TLE
class Solution {
public:
    bool canConvertString(std::string s, std::string t, int k) {
        if (s.size() != t.size()) {
            return false;
        }
        std::vector<int> counter(26, 0);
        int diff;
        for (int i = 0; i < s.size(); i++) {
            diff = (t[i] - s[i] + 26) % 26; // avoid negative
            if (diff > 0 && diff + counter[diff] * 26 > k) {
                return false;
            }
            counter[diff]++;
        }
        return true;
    }
};

/* use set will TLE
class Solution {
public:
    bool canConvertString(std::string s, std::string t, int k) {
        if (s.size() != t.size()) {
            return false;
        }
        
        std::unordered_set<int> used;
        int diff = 0;
        bool convert;
        for (int i = 0; i < s.size(); i++) {
            convert = false;
            diff = t[i] - s[i];
            if (diff != 0) {
                while (diff <= k) {
                    if (diff  > 0 && used.find(diff) == used.end()) {
                        used.insert(diff);
                        convert = true;
                        break;
                    }
                    diff += 26;
                }
                if (!convert) {
                    return false;
                }
            } 
        }
        return true;
    }
};
*/

// @lc code=end

