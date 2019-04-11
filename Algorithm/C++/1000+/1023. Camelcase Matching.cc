/*
 * Created on Thu Apr 11 2019 21:44:42
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// two pointers
#include <vector>
#include <string>
#include <cctype>


using std::vector;
using std::string;

class Solution {
 public:
  vector<bool> camelMatch(vector<string>& queries, string pattern) {
    vector<bool> result;
    for (auto q : queries) result.push_back(match(q, pattern));
    return result;
  }
 
 private:
  bool match(string query, string pattern) {
    int p1 = 0, p2 = 0, n1 = query.size(), n2 = pattern.size();
    while (p1 < n1 && p2 <= n2) {
      if (p2 == n2) {
        while (p1 < n1) {
          if (std::isupper(query[p1])) return false;
          p1++;
        }
      } else {
        while (p1 < n1 && query[p1] != pattern[p2]) {
          if (std::isupper(query[p1])) return false;
          p1++;
        }
        p1++;
        p2++;
      }
    }
    return p1 == n1 && p2 == n2;
  }
};