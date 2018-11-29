/*
 * Created on Mon Nov 26 2018 21:41:23
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// greedy, keep idx as current position to hold the next number

#include <map>

class Solution {
 public:
  int minIncrementForUnique(vector<int>& A) {
    int idx = 40000, result = 0;
    map<int, int> count;
    for(int num : A) {
      count[num]++;
      idx = std::min(num, idx);
    }
    for(auto pair : count) {
      if (idx <= pair.first) {
        result += (pair.second * (pair.second - 1)) / 2;
        idx = pair.first + pair.second;
      } else {
        result += (idx - pair.first) * pair.second + (pair.second * (pair.second - 1)) / 2;
        idx += pair.second;
      }
    }
    return result;
  }
};