/*
 * @lc app=leetcode id=93 lang=cpp
 *
 * [93] Restore IP Addresses
 */

// @lc code=start

#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> restoreIpAddresses(std::string s) {
        result.clear();
        candidate.clear();
        dfs(s, 0);
        return result;        
    }

private:
    void dfs(std::string& s, int idx) {
        if (candidate.size() > 4) return;
        if (idx == s.size() && candidate.size() == 4) {
            std::string tmp;
            for (int i = 0; i < candidate.size(); i++) {
                tmp += candidate[i];
                if (i != 3) tmp += ".";
            }
            result.push_back(tmp);
            return;
        }
        for (int i = idx; i < s.size(); i++) {
            if (is_valid(s, idx, i+1)) {
                candidate.push_back(s.substr(idx, i - idx + 1));
                dfs(s, i+1);
                candidate.pop_back();
            }
        }
    }

    bool is_valid(std::string& s, int start, int end) {
        if (end - start > 3) return false;
        if (end - start > 1) return s[start] != '0' && std::stoi(s.substr(start, end-start)) <= 255;
        return true;
    }

    std::vector<std::string> result;
    std::vector<std::string> candidate;
};
// @lc code=end

