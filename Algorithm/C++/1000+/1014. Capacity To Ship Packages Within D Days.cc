/*
 * Created on Thu Mar 21 2019 22:12:11
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// binary search

#include <vector>

class Solution {
 public:
  int shipWithinDays(std::vector<int>& weights, int D) {
    int left = 0, right = 0;
    for (auto w : weights) {
      left = std::max(left, w);
      right += w;
    }
    int mid, tmp, days;
    while (left < right) {
      mid = left + ((right - left) >> 1);
      days = 0;
      tmp = 0;
      for (auto w : weights) {
        if (tmp + w > mid) {
          days++;
          tmp = 0;
        }
        tmp += w;
      }
      days++;
      if (days > D)
        left = mid + 1;
      else
        right = mid;
    }
    return right;
  }
};