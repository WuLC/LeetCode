/*
 * Created on Thu Dec 27 2018 14:27:11
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// stack, O(n) time
#include <vector>
#include <stack>

using std::stack;
using std::vector;

class Solution {
 public:
  int sumSubarrayMins(vector<int>& A) {
    vector<int> left;
    stack<int> s;
    int n = A.size();
    for (int i = 0; i < n; i++) {
      while (!s.empty() && A[s.top()] >= A[i]) s.pop();
      if (s.empty())
        left.push_back(i + 1);
      else
        left.push_back(i - s.top());
      s.push(i);
    }

    vector<int> right;
    stack<int> rs;
    for (int i = n - 1; i >= 0; i--) {
      while (!rs.empty() && A[rs.top()] > A[i]) rs.pop();
      if (rs.empty())
        right.push_back(n - i);
      else
        right.push_back(rs.top() - i);
      rs.push(i);
    }

    long result = 0;
    const int MOD = 1000000007;
    for(int i = 0; i < n; i++) {
      result += (A[i] * left[i] * right[n - i - 1]) % MOD;
      result %= MOD;
    }
    return result;
  }
};