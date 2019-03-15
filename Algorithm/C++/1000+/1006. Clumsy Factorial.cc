/*
 * Created on Fri Mar 15 2019 16:17:50
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution, four numbers as a group

#include <cmath>

class Solution {
 public:
  int clumsy(int N) {
    int result = 0;
    bool positive = true;
    while (N > 0) {
      int tmp = 0;
      if (N > 4) {
        if (positive)
          tmp = std::floor(N * (N-1) / (N-2)) - (N-3);
        else
          tmp = std::floor(N * (N-1) / (N-2)) + (N-3);
      } else if (N == 3) {
        tmp = std::floor(N * (N-1) / (N-2));
      } else if (N == 2) {
        tmp = N * (N-1);
      } else {
        tmp = N;
      }
      result += positive? tmp: -1*tmp;
      positive = false;
      N -= 4;
    }
  return result;
  }
};