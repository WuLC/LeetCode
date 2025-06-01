#include <vector>
#include <queue>

class Solution {
public:
    int snakesAndLadders(std::vector<std::vector<int>>& board) {
        int n = board.size();
        std::queue<int> q;
        q.push(1);

        int result = 0, dest = n*n, cnt=0, curr, next;
        std::vector<bool> visited(dest+1, false);
        visited[1] = true;

        while (q.size() > 0) {
            cnt = q.size();
            while (cnt > 0) {
                curr = q.front();
                q.pop();
                if (curr >= dest) return result;
                visited[curr] = true;
                for (int i = 1; i <=6; i++) {
                    next = curr+i;
                    next = std::min(dest, next);
                    std::pair<int, int> c = getCoordinate(n, next);
                    if (board[c.first][c.second] != -1) next = board[c.first][c.second];
                    if (!visited[next]) {
                        q.push(next);
                        visited[next] = true;
                    }
                }
                cnt--;
            }
            result++;
        }
        return -1;
    }

private:
    std::pair<int, int> getCoordinate(int n, int num) {
        int r = num/n, c = num%n;
        if (c == 0) r--;

        if ((r&1) == 0) {
            c = (n+c-1)%n;
        } else {
            c = (n-c)%n;
        }
        return {n-r-1, c};
    }
};