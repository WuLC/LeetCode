/*
 * Created on Mon Apr 01 2019 23:3:40
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// stack, O(n) time, O(n) space
#include <vector>
#include <stack>
#include <utility>

class Solution {
 public:
    std::vector<int> nextLargerNodes(ListNode* head) {
      std::vector<int> result;
      std::stack<std::pair<int, int>> s;
      int count = 0;
      ListNode* p = head;
      while (p != nullptr) {
        result.push_back(0);
        while (s.size() > 0 && s.top().second < p->val) {
          result[s.top().first] = p->val;
          s.pop();
        }
        s.push(std::make_pair(count, p->val));
        count++;
        p = p->next;
      }
      return result;
    }
};