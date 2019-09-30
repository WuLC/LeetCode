#include <string>
#include <stack>
#include <algorithm>

class Solution {
 public:
  std::string removeDuplicates(std::string s, int k) {
    std::stack<char> chars;
    std::stack<int> count;
    for (char c: s) {
      if (chars.size() > 0 && chars.top() == c) {
        int tmp = count.top() + 1;
        count.pop();
        count.push(tmp);
      } else {
        chars.push(c);
        count.push(1);
      }
      if (count.top() == k) {
        count.pop();
        chars.pop();
      }
    }
    std::string result;
    while (chars.size() > 0) {
      result += std::string(count.top(), chars.top());
      count.pop();
      chars.pop();
    }
    std::reverse(result.begin(), result.end());
    return result;
  }
};