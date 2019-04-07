/*
 * Created on Sun Apr 07 2019 20:56:48
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

#include <vector>

using std::vector;

class Solution {
 public:
  vector<bool> prefixesDivBy5(vector<int>& A) {
    vector<bool> result;
    int curr = 0;
    for (auto num : A) {
      curr = (curr * 2 + num) % 5;
      if (curr == 0)
        result.push_back(true);
      else
        result.push_back(false);
    }
    return result;
  }
};