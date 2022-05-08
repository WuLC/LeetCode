/*
 * @lc app=leetcode id=76 lang=cpp
 *
 * [76] Minimum Window Substring
 */

// @lc code=start
#include <string>
#include <unordered_map>

class Solution {
public:
    std::string minWindow(std::string s, std::string t) {
        std::unordered_map<char, int> counter;
        for (auto &c:t) {
            if (counter.find(c) == counter.end()) {
                counter[c] = 0;
            }
            counter[c]++;
        }

        int left = 0, right = 0, valid_c = t.size();
        int min_start = -1, min_len = 0;
        while (right <= s.size()) {
            while (valid_c == 0) {
                if (min_start == -1 || right - left < min_len) {
                    min_start = left;
                    min_len = right - left;
                }
                if (counter.find(s[left]) != counter.end() and counter[s[left]] == 0) {
                    valid_c += 1;
                }
                counter[s[left]]++;
                left++;
            }
            if (right < s.size()) {
                if (counter.find(s[right]) != counter.end() and counter[s[right]] > 0) {
                    valid_c -= 1;
                }
                counter[s[right]]--;
            }
            right++;
        }
        if (min_len == 0) {
            return "";
        } else {
            return s.substr(min_start, min_len);
        }
    }
};
// @lc code=end

