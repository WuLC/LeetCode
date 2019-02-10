/*
 * Created on Sun Feb 10 2019 12:19:33
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// add bit by bit

#include <vector>
#include <string>

using std::vector;
using std::string;

class Solution {
 public:
  vector<int> addToArrayForm(vector<int>& A, int K) {
    string s = std::to_string(K);
    int i = A.size() - 1, j = s.size() - 1;
    int carry = 0, curr = 0, sum = 0;
    vector<int> result;
    while (i >= 0 || j >= 0) {
      if (i >= 0 && j >= 0) {
        sum = A[i] + int(s[j])-48 + carry;
      } else if (i >= 0) {
        sum = A[i] + carry;
      } else if (j >= 0) {
        sum = int(s[j])-48 + carry;
      }
      carry = sum / 10;
      curr = sum % 10;
      result.push_back(curr);
      i--;
      j--;
    }
    if (carry != 0) result.push_back(carry);
    std::reverse(result.begin(), result.end());
    return result;
  }
};