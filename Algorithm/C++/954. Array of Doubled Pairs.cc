/*
 * Created on Tue Dec 18 2018 21:57:42
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// hashmap
#include <vector>
#include <map>

using std::vector;
using std::map;

class Solution {
 public:
  bool canReorderDoubled(vector<int>& A) {
    map<int, int> counter;
    for(auto num : A)
      counter[num]++;
    for(auto it : counter) {
      int k = it.first, v = it.second;
      if (v == 0)
        continue;
      if (k < 0) {
        if (k % 2 != 0 || counter.count(k>>1) == 0 || counter[k>>1] < counter[k]){
          return false;          
        } else {
          counter[k>>1] -= counter[k];
          counter[k] = 0;
        }
      } else {
        if (counter.count(k<<1) == 0 || counter[k<<1] < counter[k]) {
          return false;
        } else {
          counter[k<<1] -= counter[k];
          counter[k] = 0;
        }
      }
    }
    return true;
  }
};