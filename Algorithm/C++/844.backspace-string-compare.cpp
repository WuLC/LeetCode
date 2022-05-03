/*
 * @lc app=leetcode id=844 lang=cpp
 *
 * [844] Backspace String Compare
 */

// @lc code=start

#include <string>

class Solution {
public:
    bool backspaceCompare(std::string s, std::string t) {
        int s_len = helper(s), t_len = helper(t);
        if (s_len != t_len) {
            return false;
        } else {
            for (int i = s.size()-1, j = t.size()-1; 
                     i >= s.size() - s_len && j >= t.size() - t_len; 
                     i--, j--) {
                if (s[i] != t[j]) {
                    return false;
                }
            }
        }
        return true;
    }

private:
    int helper(std::string& s) {
        int p = s.size() - 1, skip = 0, len=0;
        for (int i=s.size() - 1; i >= 0; i--) {
            if (s[i] == '#') {
                skip++;
            } else if (skip > 0) {
                skip--;
            } else {
                s[p] = s[i];
                p--;
                len++;
            }
        }
        return len;
    }    
};
// @lc code=end

