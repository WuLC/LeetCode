/*
 * Created on Thu Jan 03 2019 15:5:1
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// recursive
#include <vector>
#include <string>

using std::vector;
using std::string;

class Solution {
 public:
  vector<int> numsSameConsecDiff(int N, int K) {
    vector<int> result;
    if (N == 1) {
      for (int i = 0; i < 10; i++)
        result.push_back(i);
    } else {
      for (int i = 1; i < 10; i++) 
        for (auto num : generate(i, N, K)) 
          result.push_back(std::stoi(num));
    }
    return result;
  }

  vector<string> generate(int digit, int N, int K) {
    vector<string> tmp;
    if (N == 1) {
      tmp.push_back(std::to_string(digit));
      return tmp;
    }
    if (digit - K >= 0) {
      for (auto e : generate(digit - K, N - 1, K))
        tmp.push_back(std::to_string(digit) + e);
    }
    if (K != 0 && digit + K < 10) {
      for (auto e : generate(digit + K, N - 1, K)) 
        tmp.push_back(std::to_string(digit) + e);
    }
    return tmp;
  }
};