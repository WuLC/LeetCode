/*
 * Created on Mon Dec 24 2018 13:51:49
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

#include <vector>
#include <set>

using std::vector;
using std::set;

class Solution {
 public:
  int repeatedNTimes(vector<int>& A) {
    set<int> appeared;
    for (auto num : A) {
      if (appeared.count(num) > 0)
       return num;
      appeared.insert(num);
    }
    return -1;
  }
};