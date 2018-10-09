/*
 * Created on Tue Oct 09 2018 11:18:53
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp, O(n) time, find the minSubarray for the circular case
// referer: https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/C++JavaPython-One-Pass
class Solution {
public:
  int maxSubarraySumCircular(vector<int>& A) {
    int sub_max = A[0], sub_min = A[0];
    int curr_max = A[0], curr_min = A[0];
    int max_num = A[0], sum = A[0];
    for(int i = 1; i < A.size(); i++) {
      curr_max = std::max(A[i], A[i] + curr_max);
      curr_min = std::min(A[i], A[i] + curr_min);
      sub_max = std::max(sub_max, curr_max);
      sub_min = std::min(sub_min, curr_min);
      max_num = std::max(max_num, A[i]);
      sum += A[i];
    }
    if (sub_min == sum)
      return std::max(max_num, sub_max);
    else
      return std::max(sub_max, sum - sub_min);
  }
};