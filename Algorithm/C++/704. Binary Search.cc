/*
 * Created on Thu Dec 20 2018 16:15:48
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

#include <vector>

using std::vector;

class Solution {
 public:
  int search(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    while (left <= right) {
      int mid = left + ((right - left) >> 1);
      if (nums[mid] == target) {
        return mid;
      } else if (nums[mid] > target) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
    return -1;
  }
};