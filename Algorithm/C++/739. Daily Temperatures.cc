/*
 * Created on Fri Dec 28 2018 13:3:56
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// stack, O(n) time
#include <vector>
#include <stack>

using std::stack;
using std::vector;

class Solution {
 public:
  vector<int> dailyTemperatures(vector<int>& T) {
    vector<int> result;
    stack<int> s;
    for (int i = T.size() - 1; i >= 0; i--) {
      while (s.size() > 0 && T[s.top()] <= T[i]) s.pop();
      result.push_back(s.size() > 0? s.top() - i: 0);
      s.push(i);
      }
    std::reverse(result.begin(), result.end());
    return result;
  }
};