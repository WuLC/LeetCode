/*
 * Created on Wed Oct 31 2018 19:59:54
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// record prefix sum, applicable to not just 0 and 1
class Solution {
 public:
    int numSubarraysWithSum(vector<int>& A, int S) {
      int result = 0, curr_sum = 0;
      unordered_map<int, int> count;
      count[0] = 1;
      for(int num : A) {
        curr_sum += num;
        result += count[curr_sum - S];
        count[curr_sum] += 1;
      }
      return result;
    }
};