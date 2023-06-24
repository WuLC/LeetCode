/*
 * @lc app=leetcode id=950 lang=cpp
 *
 * [950] Reveal Cards In Increasing Order
 */

// @lc code=start

#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    std::vector<int> deckRevealedIncreasing(std::vector<int>& deck) {
        std::sort(deck.begin(), deck.end());
        std::vector<int> result(deck.size());
        std::queue<int> q;
        for (int i = 0; i < deck.size(); ++i) {
            q.push(i);
        }
        for (int i = 0; i < deck.size(); ++i) {
            result[q.front()] = deck[i];
            q.pop();
            q.push(q.front());
            q.pop();
        }
        return result;
    }
};
// @lc code=end

