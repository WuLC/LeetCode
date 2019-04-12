/*
 * Created on Fri Apr 12 2019 22:14:54
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// set
#include <string>
#include <unordered_set>

class Solution {
 public:
  bool queryString(std::string S, int N) {
    std::unordered_set<int> result, next;
    result.insert(0);
    next.insert(0);
    for (char c : S) {
      int bit = c - '0';
      std::unordered_set<int> curr(next.begin(), next.end());
      next.clear();
      next.insert(0);
      for (auto num : curr) {
        int val = (num << 1) + bit;
        if (val <= N) {
          result.insert(val);
          next.insert(val);
        }
      }
      if (result.size() == N + 1) return true;
    }
    return false;
  }
};