#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num_set(nums.begin(), nums.end());
        int max_len = 0;

        for (int num : num_set) {
            if (num_set.find(num - 1) == num_set.end()) {
                int curr_num = num;
                int curr_len = 1;

                while (num_set.find(curr_num + 1) != num_set.end()) {
                    curr_num++;
                    curr_len++;
                }

                max_len = max(max_len, curr_len);
            }
        }
        return max_len;
    }
};

// Test
#include <iostream>
int main() {
    Solution sol;
    vector<int> v = {100,4,200,1,3,2};
    cout << sol.longestConsecutive(v) << endl;
    return 0;
}
