/*
 * Created on Sun Nov 04 2018 11:2:8
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// count the number of two sum
// O(n^2) time complexity
class Solution {
 public:
    int threeSumMulti(vector<int>& A, int target) {
      unordered_map<int, int> counter;
      int result = 0;
      for(int i = 0; i < A.size(); i++) {
        result = (result + counter[target - A[i]]) % 1000000007;
        for(int j = 0; j < i; j++) {
          counter[A[i] + A[j]]++;
        }
      }
      return result;
    }
};
