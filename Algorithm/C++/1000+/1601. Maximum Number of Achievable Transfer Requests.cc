#include <vector>
#include <algorithm>

class Solution {
public:
    int maximumRequests(int n, std::vector<std::vector<int>>& requests) {
        result=0;
        std::vector<int> record(n, 0);
        dfs(0, requests, record, 0);
        return result;
    }

    void dfs(int idx, std::vector<std::vector<int>>& requests, std::vector<int> record, int cnt) {
        if(std::all_of(record.begin(), record.end(), [](const int& a){return a==0;})) {
            result = std::max(result, cnt);
        }
        for(int i = idx; i < requests.size(); i++) {
            record[requests[i][0]]--;
            record[requests[i][1]]++;
            dfs(i+1, requests, record, cnt+1);
            record[requests[i][0]]++;
            record[requests[i][1]]--;
        }
    }

private:
    int result;
};