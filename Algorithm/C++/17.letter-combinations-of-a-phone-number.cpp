/*
 * @lc app=leetcode id=17 lang=cpp
 *
 * [17] Letter Combinations of a Phone Number
 */

// @lc code=start

#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> letterCombinations(std::string digits) {
        result.clear();
        candidate = "";
        backtrack(digits, 0);
        return result;
    }

private:
    std::vector<std::string> result;
    std::string candidate;
    const string letterMap[10] = {
        "", // 0
        "", // 1
        "abc", // 2
        "def", // 3
        "ghi", // 4
        "jkl", // 5
        "mno", // 6
        "pqrs", // 7
        "tuv", // 8
        "wxyz", // 9
    };
    
    void backtrack(std::string& digits, int idx) {
        if (digits.size() == 0) return;
        if (idx == digits.size()) {
            result.push_back(candidate);
            return;
        }
        int num = digits[idx] - '0';
        for (auto c: letterMap[num]) {
            candidate += c;
            backtrack(digits, idx+1);
            candidate = candidate.substr(0, candidate.size()-1);
        }
    }
    
};
// @lc code=end

