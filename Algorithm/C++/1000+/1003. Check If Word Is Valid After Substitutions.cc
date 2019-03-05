/*
 * Created on Tue Mar 05 2019 18:0:9
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// iterate from left to right, there should always be #a>#b>#c
#include <string>
#include <unordered_map>

class Solution {
 public:
  bool isValid(std::string S) {
    std::unordered_map<char, int> counter;
    for (auto c : S) {
      counter[c]++;
      if (!(counter['a']>=counter['b'] && counter['b']>=counter['c'])) return false;
    }
    if (counter['a']==counter['b'] && counter['b']==counter['c']) {
      return true;
    } else {
      return false;
    }
  }
};
