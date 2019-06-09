/*
 * Created on Sun Jun 09 2019 18:26:26
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// stack
#include <string>
#include <stack>
#include <unordered_set>
#include <unordered_map>

class Solution {
 public:
  std::string smallestSubsequence(std::string text) {
    std::unordered_map<char, int> counter;
    std::stack<char> s;
    std::unordered_set<char> stored;
    for (char c : text)
      counter[c]++;
    for (char c : text) {
      if (stored.find(c) != stored.end()) {
        counter[c]--;
        continue;
      }
      while (s.size() > 0 && int(s.top()) > int(c) && counter[s.top()] > 1) {
        counter[s.top()] -= 1;
        stored.erase(s.top());
        s.pop();
      }
      s.push(c);
      stored.insert(c);
    }
    int i = s.size();
    vector<char> tmp(i, ' ');
    while (!s.empty()) {
      tmp[i-1] = s.top();
      i--;
      s.pop();
    }
    return std::string(tmp.begin(), tmp.end());
  }
};