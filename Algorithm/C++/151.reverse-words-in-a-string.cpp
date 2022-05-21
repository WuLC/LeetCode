/*
 * @lc app=leetcode id=151 lang=cpp
 *
 * [151] Reverse Words in a String
 */

// @lc code=start

#include <string>

class Solution {
public:
    std::string reverseWords(std::string s) {
        removeExtraSpaces(s);
        reverseStr(s, 0, s.size()-1);

        // reverse word by word
        int p1 = 0, p2 = 0;
        while (p2 <= s.size()) {
            if (p2 == s.size() || s[p2] == ' ') {
                reverseStr(s, p1, p2-1);
                p1 = p2+1;
            }
            p2++;
        }
        return s;
    }

    void removeExtraSpaces(std::string& s) {
        int slow = 0, fast = 0;
        while (fast < s.size()) {
            if (s[fast] == ' ') {
                if (slow > 0 && s[slow-1] != ' ') {
                    s[slow] = ' ';
                    slow++;
                }
                fast++;
            } else {
                s[slow++] = s[fast++];
            }
            // std::cout << s << std::endl;
        }
        if (s[slow-1] == ' ') {
            s.resize(slow-1);
        } else {
            s.resize(slow);
        }
        // std::cout << "resized str: " << s;
    }

    void reverseStr(std::string& s, int start, int end) {
        while (start < end) {
            std::swap(s[start++], s[end--]);
        }
    }
};
// @lc code=end

