/*
 * @lc app=leetcode id=239 lang=cpp
 *
 * [239] Sliding Window Maximum
 */

// @lc code=start

#include <vector>
#include <memory>


// use doubly-linked list
struct DoublyListNode {
    DoublyListNode(int val): index(val) {};
    int index;
    std::shared_ptr<DoublyListNode> pre = nullptr;
    std::shared_ptr<DoublyListNode> next = nullptr;
};

class Solution {
public:
    std::vector<int> maxSlidingWindow(std::vector<int>& nums, int k) {
        if (nums.size() <= 1 || k == 1) return nums;
        std::vector<int> result;
        std::shared_ptr<DoublyListNode> head = std::make_shared<DoublyListNode>(0), tail;
        tail = head;
        for (int i = 1; i < nums.size(); i++) {
            while(tail != nullptr && nums[i] > nums[tail->index]) tail = tail->pre;

            if (tail == nullptr) { // all pop out
                tail = std::make_shared<DoublyListNode>(i);
                head = tail;
            } else { 
                tail->next = std::make_shared<DoublyListNode>(i);
                tail->next->pre = tail;
                tail = tail->next;
            }

            if (i - head->index >= k) {
                head = head->next;
                head->pre = nullptr;
            }
            if (i >= k-1) result.push_back(nums[head->index]);
        }
        return result;
    }
};
// @lc code=end

