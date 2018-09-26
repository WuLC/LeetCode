/*
 * Created on Tue Sep 25 2018 16:0:9
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// binary search
class TopVotedCandidate {
public:
    map<int, int> leaders;
    TopVotedCandidate(vector<int> persons, vector<int> times) {
        unordered_map<int, int> counter;
        int n = persons.size(), lead = -1;
        for(int i = 0; i < n; i++) {
            leaders[times[i]] = persons[i];
        }
        for(auto it:leaders) {
            if (++counter[it.second] >= counter[lead]) {
                lead = it.second;
            }
            leaders[it.first] = lead;
        }
    }
    
    int q(int t) {
        return (--leaders.upper_bound(t))->second;
    }
};

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.q(t);
 */