/*
 * Created on Sun Apr 07 2019 20:25:25
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

 // bit manipulation
 
#include <string>


class Solution {
 public:
  std::string baseNeg2(int N) {
    if (N == 0) return "0";
    std::string result = "";
    int idx = 0, curr = 0, carry = 0;
    while (N > 0 || carry > 0) {
      int s = (N&1) + carry;
      curr = s % 2;
      carry = s / 2;
      result = std::to_string(curr) + result;
      if ((idx&1) > 0 && curr > 0) carry = 1;
      N >>= 1;
      idx++;
    }
    return result;
  }
};
