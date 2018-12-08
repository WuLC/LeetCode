/*
 * Created on Sat Dec 08 2018 16:30:39
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// permutation
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
 public:
  string largestTimeFromDigits(vector<int>& A) {
      permute(A, 0, A.size() - 1);
      return result;
  }

 private:
  string result = "";
  void permute(vector<int>& A, int left, int right) {
    if (left == right) {
      if (A[0] * 10 + A[1] < 24 && A[2] < 6) {
        std::stringstream ss;
        for(int i = 0; i < A.size(); i++) {
          if (i == 2) ss << ":";
          ss << A[i];
        }
        result = std::max(result, ss.str());
      }
    } else {
      for (int i = 0; left + i <= right; i++) {
        std::swap(A[left], A[left + i]);
        permute(A, left + 1, right);
        std::swap(A[left], A[left + i]);
      }
    }
  }
};