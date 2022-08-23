/*
 * @lc app=leetcode id=738 lang=cpp
 *
 * [738] Monotone Increasing Digits
 */

// @lc code=start
#include <string>
#include <vector>

class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        std::string s = std::to_string(n);
        std::vector<int> digits;
        for (int i = 0; i < s.size(); i++) {
            if (i+1 < s.size() && s[i] > s[i+1]) {
                digits.push_back(s[i] - '1');
                while (++i < s.size()) {
                    digits.push_back(9);
                }
            } else {
                digits.push_back(s[i] - '0');
            }
        }

        for (int i = digits.size() - 1; i > 0; i--) {
            if (digits[i] < digits[i-1]) {
                digits[i-1] = digits[i];
                digits[i] = 9;
            }
        }

        int result = 0;
        for (auto d : digits) {
            result = result * 10 + d;
        }
        return result;
    }
};
// @lc code=end

