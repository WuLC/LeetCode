/*
 * Created on Fri Dec 14 2018 14:35:58
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// compare char by char, pay attention to the case when one word is the prefix of another word
#include <vector>
#include <string>
#include <unordered_map>

using std::vector;
using std::string;
using std::unordered_map;

class Solution {
 public:
  bool isAlienSorted(vector<string>& words, string order) {
    unordered_map<char, int> order_num;
    for(int i = 0; i < order.size(); i++) {
      order_num[order[i]] = i;
    }

    for (int i = 0; i < words.size() - 1; i++) {
      bool equal = true;
      for (int j = 0; j < std::min(words[i].size(), words[i+1].size()); j++) {
        if(order_num[words[i][j]] < order_num[words[i+1][j]]) {
          equal = false;
          break;
        } else if(order_num[words[i][j]] > order_num[words[i+1][j]]) {
          return false;
        }
      }
      if (equal && words[i].size() > words[i+1].size()) {
        return false;
      }
    }
    return true;
  }
};