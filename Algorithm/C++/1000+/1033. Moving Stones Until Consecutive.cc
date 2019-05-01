/*
 * Created on Wed May 01 2019 17:41:6
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

#include <vector>

class Solution {
 public:
  std::vector<int> numMovesStones(int a, int b, int c) {
      std::vector<int> nums {a, b, c};
      std::sort(nums.begin(), nums.end());
      int min_move, max_move;
      if (nums[2] - nums[1] == 2 || nums[1] - nums[0] == 2)
        min_move = 1;
      else
        min_move = std::min(1, nums[1] - nums[0] - 1) + std::min(1, nums[2] - nums[1] - 1);
      max_move = nums[2] - nums[0] - 2;
      return vector<int> {min_move, max_move};
  }
};
