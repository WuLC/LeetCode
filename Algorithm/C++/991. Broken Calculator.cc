/*
 * Created on Tue Feb 12 2019 20:22:27
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// chang Y to X
// greedy: when Y is odd, perform Y-1, else perform Y/2

class Solution {
 public:
  int brokenCalc(int X, int Y) {
    if (X >= Y) {
      return X-Y;
    } else {
      return (Y&1) == 1? 1 + brokenCalc(X, Y+1): 1 + brokenCalc(X, Y>>1); 
    }
  }
};