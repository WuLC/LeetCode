/*
 * @lc app=leetcode id=1047 lang=cpp
 *
 * [1047] Remove All Adjacent Duplicates In String
 */

// @lc code=start

#include <string>
#include <stack>

class Solution {
public:
    std::string removeDuplicates(std::string s) { 
        std::stack<char> _stack;
        for (auto c : s) {
            if (!_stack.empty() && _stack.top() == c) {
                _stack.pop();
            } else {
                _stack.push(c);
            }
        }
        int len = _stack.size(), idx = _stack.size() - 1;
        std::string result(len, ' ');
        while(!_stack.empty()) {
            result[idx--] = _stack.top();
            _stack.pop();
        }
        return result;
    }
};
// @lc code=end

