/*
 * Created on Tue Oct 23 2018 16:44:56
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// two pointers
class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
      int p1 = 0, p2 = 1, n = A.size();
      while(p1 < n && p2 < n) {
        while(p1 < n && (A[p1]&1) == 0) p1 += 2;
        while(p2 < n && (A[p2]&1) == 1) p2 += 2;
        if (p1 < n && p2 < n) std::swap(A[p1], A[p2]);
      }
      return A;
    }
};