/*
 * Created on Sat Jan 12 2019 14:29:59
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */
#include <vector>

using std::vector;

class Solution {
 public:
  int rob(vector<int>& nums) {
    int previous = 0, curr = 0;
    for (int num: nums) {
      int tmp = std::max(curr, previous + num);
      previous = curr;
      curr = tmp;
    }
    return curr;
  }
};