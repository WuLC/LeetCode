/*
 * Created on Mon Dec 24 2018 19:27:35
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// stack, O(n) time

#include <vector>
#include <stack>

using std::vector;
using std::stack;

class Solution {
 public:
  int maxWidthRamp(vector<int>& A) {
    stack<int> decreased;
    decreased.push(0);
    for (int i = 1; i < A.size(); i++) {
      if (A[i] < A[decreased.top()])
        decreased.push(i);
    }
    int result = 0;
    for (int i = A.size() - 1; i >= 0; i--) {
      while (decreased.size() > 0 && A[i] >= A[decreased.top()]) {
        result = std::max(result, i - decreased.top());
        decreased.pop();
      }
      if (decreased.size() == 0) break;
    }
    return result;
  }
};