/*
 * @lc app=leetcode id=131 lang=cpp
 *
 * [131] Palindrome Partitioning
 */

// @lc code=start

#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::vector<std::string>> partition(std::string s) {
        result.clear();
        candidate.clear();
        backtrack(s, 0);
        return result;
    }

private:
    bool isPalindorme(std::string& s, int left, int right) {
        while(left < right) {
            if (s[left++] != s[right--]) return false;
        }
        return true;
    }

    void backtrack(std::string& s, int idx) {
        if (idx == s.size()) {
            result.push_back(candidate);
            return;
        }
        for (int i = idx; i < s.size(); i++) {
            if (isPalindorme(s, idx, i)) {
                candidate.push_back(s.substr(idx, i - idx + 1));
                backtrack(s, i+1);
                candidate.pop_back();
            }
        }
    }

    std::vector<std::vector<std::string>> result;
    std::vector<std::string> candidate;
};

// @lc code=end

