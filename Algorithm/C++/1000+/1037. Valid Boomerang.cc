/*
 * Created on Sun May 05 2019 17:9:47
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

#include <vector>

using std::vector;

class Solution {
 public:
  bool isBoomerang(vector<vector<int>>& points) {
    vector<int> p1 = points[0], p2 = points[1], p3 = points[2];
    return (p2[1] - p1[1]) * (p3[0] - p2[0]) != (p2[0] - p1[0]) * (p3[1] - p2[1])
  }
};