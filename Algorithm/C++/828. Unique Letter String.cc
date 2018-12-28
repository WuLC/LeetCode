/*
 * Created on Fri Dec 28 2018 10:12:29
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// two pointers
#include <string>

using std::string;

class Solution {
 public:
  int uniqueLetterString(string S) {
    int result = 0;
    const int MOD = 1000000007;
    int left, right;
    for(int i = 0; i < S.size(); i++) {
      left = i - 1;
      right = i + 1;
      while (left >= 0 && S[left] != S[i]) left--;
      while (right < S.size() && S[right] != S[i]) right++;
      result += ((i - left) * (right - i)) % MOD;
      result %= MOD;
    }
    return result;
  }
};