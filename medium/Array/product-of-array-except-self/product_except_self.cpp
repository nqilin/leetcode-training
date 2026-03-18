#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);

        // Prefix
        int prefix = 1;
        for (int i = 0; i < n; ++i) {
            res[i] = prefix;
            prefix *= nums[i];
        }

        // Suffix
        int suffix = 1;
        for (int i = n-1; i >= 0; --i) {
            res[i] *= suffix;
            suffix *= nums[i];
        }

        return res;
    }
};

// Test
#include <iostream>
int main() {
    Solution sol;
    vector<int> v = {1,2,3,4};
    auto ans = sol.productExceptSelf(v);
    for (int x : ans) cout << x << " ";
    return 0;
}
