/*
 * Created on Tue Apr 23 2019 22:47:30
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// dp, O(nlgn) time, O(n) space
// next great element with TreeMap
// map::lower_bound returns an iterator pointing to the first element that is not less than key.
// map::upper_bound returns an iterator pointing to the first element that is greater than key.

#include <vector>
#include <map>

class Solution {
 public:
  int oddEvenJumps(std::vector<int>& A) {
    int n = A.size();
    std::vector<bool> odd_dp(n, false), even_dp(n, false);
    std::map<int, int> m;
    odd_dp[n-1] = true;
    even_dp[n-1] = true;
    int result = 1;
    for (int i = n - 1; i >= 0; i--) {
      auto greater = m.lower_bound(A[i]);
      if (greater != m.end() && even_dp[greater->second]) {
        result++;
        odd_dp[i] = true;
      }
      auto smaller = m.upper_bound(A[i]);
      if (smaller != m.begin() && odd_dp[(--smaller)->second]) even_dp[i] = true;
      m[A[i]] = i;
    }
    return result;
  }
};