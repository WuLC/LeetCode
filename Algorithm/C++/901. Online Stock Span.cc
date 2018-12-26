/*
 * Created on Wed Dec 26 2018 16:58:25
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// keep increasing elements in a stack
#include <stack>
#include <vector>

using std::vector;
using std::stack;

class StockSpanner {
 public:
  StockSpanner() {
    count = 0;
  }

  int next(int price) {
    count++;
    while (!indices.empty() && indices.top()[0] <= price) {
      indices.pop();
    }
    int result = count;
    if (!indices.empty()) {
      result = count - indices.top()[1];
    }
    indices.push(vector<int>{price, count});
    return result;
  }

 private:
  stack<vector<int>> indices;
  int count;
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */