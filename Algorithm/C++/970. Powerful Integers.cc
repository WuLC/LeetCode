/*
 * Created on Sun Jan 06 2019 21:29:53
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// generate candidate for x^i and y^j seperately and add them up
#include <vector>
#include <set>

using std::vector;
using std::set;
using std::pow;

class Solution {
 public:
  vector<int> powerfulIntegers(int x, int y, int bound) {
    vector<int> candidate_x{1}, candidate_y{1};
    int count = 1;
    long tmp_x = x, tmp_y = y;
    while ((x != 1 && tmp_x < bound) || (y != 1 && tmp_y < bound)) {
      count++;
      if (x != 1 && tmp_x < bound) {
        candidate_x.push_back(tmp_x);
        tmp_x = pow(x, count);
      }
      if (y != 1 && tmp_y < bound) {
        candidate_y.push_back(tmp_y);
        tmp_y = pow(y, count);
      }
    }

    set<int> result;
    for (int i = 0; i < candidate_x.size(); i++) {
      for (int j = 0; j < candidate_y.size(); j++) {
        if (candidate_x[i] + candidate_y[j] > bound) break;
        result.insert(candidate_x[i] + candidate_y[j]);
      }
    }
    return vector<int>(result.begin(), result.end());
    }
};