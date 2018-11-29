/*
 * Created on Thu Nov 29 2018 20:37:27
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// greedy
#include <vector>
class Solution {
 public:
  int bagOfTokensScore(vector<int>& tokens, int P) {
    std::sort(tokens.begin(), tokens.end());
    vector<int> prefix_sum;
    int result = 0, curr = 0;
    for(int t : tokens) {
      curr += t;
      prefix_sum.push_back(curr);
      if (curr < P) result++;
    }

    int p1 = 0, p2 = tokens.size() - 1;
    while (p1 < p2) {
      if (P < tokens[p1]) break;
      P += tokens[p2--] - tokens[p1++];
      for (int i = p2; i > p1 - 1; i--) {
        if (P >= prefix_sum[i] - prefix_sum[p1-1]) {
          result = std::max(result, i - p1 + 1);
          break;
        }
      }
    }
    return result;
  }
};