/*
 * Created on Fri Feb 01 2019 8:46:16
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp, O(n) time, O(n) space
#include <vector>

using std::vector;

class Solution {
 public:
  int mincostTickets(vector<int>& days, vector<int>& costs) {
    vector<int> dp{0};
    for (int i=0; i < days.size(); ++i) {
      dp.push_back(dp[i] + costs[0]);
      for (int j=i-1; j >= std::max(0, i - 30); --j) {
        if (days[j] > days[i] - 7) dp[i+1] = std::min(dp[i+1], dp[j] + costs[1]);
        if (days[j] > days[i] - 30) dp[i+1] = std::min(dp[i+1], dp[j] + costs[2]);
        if (days[j] <= days[i] - 30) break;
      }
    }
    return dp[dp.size()-1];
  }
};