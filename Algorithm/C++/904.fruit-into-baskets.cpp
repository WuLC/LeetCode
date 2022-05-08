 /*
 * @lc app=leetcode id=904 lang=cpp
 *
 * [904] Fruit Into Baskets
 */

// @lc code=start
#include <vector>
#include <unordered_map>

class Solution {
public:
    int totalFruit(std::vector<int>& fruits) {
        int left = 0, right = 0, result = 0, valid_fruit = 0;
        std::unordered_map<int,int> counter;
        while (right <= fruits.size()) {
            while (valid_fruit > 2) {
                counter[fruits[left]]--;
                if (counter[fruits[left]] == 0) {
                    valid_fruit--;
                }
                left++;
            }
            result = std::max(result, right - left);
            if (right < fruits.size()) {
                if (counter.find(fruits[right]) == counter.end() ||
                    counter[fruits[right]] == 0) {
                        valid_fruit++;
                    }
                counter[fruits[right]]++;
            }
            right++;
        }
        return result;
    }
};
// @lc code=end

