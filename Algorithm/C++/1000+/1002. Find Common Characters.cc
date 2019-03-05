/*
 * Created on Tue Mar 05 2019 16:34:10
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution
// be careful erasing element in map while iterating it 

#include <vector>
#include <unordered_map>
#include <string>

using std::vector;
using std::string;
using std::unordered_map;

class Solution {
 public:
  vector<string> commonChars(vector<string>& A) {
    unordered_map<char, int> curr;
    unordered_map<char, int> tmp;
    for(int i = 0; i < A.size(); ++i){
      if (i == 0) {
        for (auto c : A[i]) curr[c]++;
      } else {
        tmp.clear();
        for (auto c : A[i]) tmp[c]++;
        // erasing map while iterating it 
        for (auto it = curr.begin(); it != curr.end();) {
          if (tmp.count(it->first) > 0) {
            it->second = std::min(it->second, tmp[it->first]);
            ++it;
          } else {
            curr.erase(it++);
          }
        }
      }
    }
    vector<string> result;
    for (auto e : curr) {
      while (e.second > 0) {
        result.push_back(string(1, e.first));
        e.second--;
      }
    }
    return result;
  }
};