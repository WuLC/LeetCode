/*
 * Created on Tue Apr 09 2019 11:1:14
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// stack
#include <string>
#include <stack>


class Solution {
 public:
  std::string removeOuterParentheses(std::string S) {
    std::stack<int> s;
    std::string result;
    for (int i = 0; i < S.size(); ++i) {
      if (S[i] == '(') {
        s.push(i);
      } else {
        int idx = s.top();
        s.pop();
        if (s.size() == 0) {
          result += S.substr(idx+1, i-idx-1);
        }
      }
    }
    return result;
  }
};