/*
 * Created on Thu Mar 21 2019 9:26:44
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// bit manipulation, pay attention that the priority of == is grater than &

#include <cmath>

class Solution {
 public:
  int bitwiseComplement(int N) {
    if (N == 0) return 1;
    int count = 0, n = N;
    while (n > 0) {
      if ((n&1) == 1) count++;
      n >>= 1;
    }
    int result = 0, bit = 0;
    while (count > 0) {
      if ((N&1) == 0) 
        result += std::pow(2, 1*bit); // why does (1<<bit) is slower?
      else
        count--;
      bit++;
      N >>= 1;
    }
    return result;
  }
};