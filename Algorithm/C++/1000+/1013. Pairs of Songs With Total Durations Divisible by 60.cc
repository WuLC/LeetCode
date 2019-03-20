/*
 * Created on Wed Mar 20 2019 21:19:49
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// O(n) time, simple solution

#include <vector>

class Solution {
  public:
    int numPairsDivisibleBy60(std::vector<int>& time) {
      std::vector<int> count(60, 0);
      int result = 0;
      for (auto t : time) {
        result += count[(60 - (t%60)) % 60];
        count[t % 60]++;
      }
      return result;
    }
};

// faster solution
class Solution {
  public:
    int numPairsDivisibleBy60(std::vector<int>& time) {
      std::vector<int> count(60, 0);
      for (auto t : time) count[t % 60]++;
      int result = 0;
      for (int i = 0; i <= 30; ++i) {
        if (i == 0 || i == 30)
          result += (count[i]*(count[i]-1))/2;
        else
          result += count[i]*count[60-i];
      }
      return result;
    }
};