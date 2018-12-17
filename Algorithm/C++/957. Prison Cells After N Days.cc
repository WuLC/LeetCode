/*
 * Created on Sun Dec 16 2018 20:19:59
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// hashmap, there always exists a loop 
#include <vector>
#include <unordered_map>
#include <string>

using std::vector;
using std::unordered_map;
using std::string;

class Solution {
 public:
  vector<int> prisonAfterNDays(vector<int>& cells, int N) {
    unordered_map<string, int> record;
    unordered_map<int, vector<int>> reversed_record;
    vector<int> curr(cells);
    for (int i = 0; i < N; i++) {
      std::stringstream ss;
      for(auto digit:curr) ss << char(digit);
      string s = ss.str();
      if (record.count(s) > 0) {
        int left = (N - record[s]) % (i - record[s]);
        return reversed_record[record[s] + left];
      } else {
        record[s] = i;
        reversed_record[i] = curr;
      }

      // iterate
      vector<int> next(8, 0);
      for (int j = 1; j < 7; j++)
        next[j] = curr[j-1] == curr[j+1]? 1: 0;
      curr = next;
    }
    return curr;
  }
};