#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> st;
        for (int num : nums) {
            if (st.find(num) != st.end()) {
                return true;
            }
            st.insert(num);
        }
        return false;
    }
};

// Test
#include <iostream>
int main() {
    Solution sol;
    vector<int> nums = {1,2,3,1};
    cout << sol.containsDuplicate(nums) << endl;
    return 0;
}
