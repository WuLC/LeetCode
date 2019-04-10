/*
 * Created on Wed Apr 10 2019 17:4:23
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */



#include <vector>
#include <map>


class Solution {
 public:
  int videoStitching(std::vector<std::vector<int>>& clips, int T) {
    std::map<int, int> record;
    for (auto c : clips) record[c[0]] = std::max(record[c[0]], c[1]);
    int curr = 0, next = 0, count = 0;
    for (auto c : record) {
      if (curr >= T || next < c.first) break;
      if (curr < c.first) {
        count++;
        curr = next;
      }
      next = std::max(next, c.second);
    }
    if (curr >= T) {
      return count;
    } else if (next >= T) {
      return count + 1;
    } else {
      return -1;
    }
  }
};