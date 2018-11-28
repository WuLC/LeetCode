/*
 * Created on Wed Nov 28 2018 9:38:18
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// two pointers
#include <stack>
class Solution {
 public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
      stack<int> nums;
      int p1 = 0, p2 = 0;
      while (p1 < pushed.size() && p2 < popped.size()) {
        if (pushed[p1] == popped[p2]) {
          p1++;
          p2++;
        } 
        else if (nums.size() > 0 && nums.top() == popped[p2]) {
          nums.pop();
          p2++;
        }
        else {
          while (p1 < pushed.size() && pushed[p1] != popped[p2])
            nums.push(pushed[p1++]);
        }
      }
      while (p2 < popped.size() && nums.size() > 0 && nums.top() == popped[p2]) {
        nums.pop();
        p2++;
      }
      return p2 == popped.size();
    }
};