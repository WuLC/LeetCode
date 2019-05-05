/*
 * Created on Sun May 05 2019 15:48:59
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// sort with custom function
#include <vector>

using std::vector;

class Solution {
 public:
  int twoCitySchedCost(vector<vector<int>>& costs) {
    std::sort(begin(costs), end(costs), [](vector<int> &v1, vector<int> &v2) {
      return (v1[0] - v1[1] < v2[0] - v2[1]);
    });
    int result = 0;
    for (int i = 0; i < (costs.size() >> 1); ++i) {
      result += costs[i][0] + costs[i + （cs.size() >> 1)][1];
    }
    return result;
  }
};