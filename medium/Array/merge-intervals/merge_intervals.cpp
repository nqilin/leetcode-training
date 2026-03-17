#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> res;
        res.push_back(intervals[0]);
        
        for (int i = 1; i < intervals.size(); ++i) {
            auto& last = res.back();
            auto& curr = intervals[i];
            
            if (curr[0] <= last[1]) {
                last[1] = max(last[1], curr[1]);
            } else {
                res.push_back(curr);
            }
        }
        return res;
    }
};

// Test
#include <iostream>
int main() {
    Solution sol;
    vector<vector<int>> v = {{1,3},{2,6},{8,10},{15,18}};
    auto ans = sol.merge(v);
    for (auto& p : ans) {
        cout << p[0] << "," << p[1] << " ";
    }
    return 0;
}
