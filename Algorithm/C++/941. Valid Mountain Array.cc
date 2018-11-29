/*
 * Created on Fri Nov 23 2018 22:15:59
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// assume two people climb from two side and stop at their peak
// return true when their peaks are the same
class Solution {
 public:
  bool validMountainArray(vector<int>& A) {
    int n = A.size();
    int left = 0, right = n - 1;
    while (left + 1 < n && A[left] < A[left + 1]) left++;
    while (right - 1 >= 0 && A[right] < A[right - 1]) right--;
    return left == right && left != 0 && right != n-1;
  }
};