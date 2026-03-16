#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty()) return 0;

        int max_prod = nums[0];
        int min_prod = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            int temp = max_prod;
            max_prod = max({nums[i], max_prod * nums[i], min_prod * nums[i]});
            min_prod = min({nums[i], temp * nums[i], min_prod * nums[i]});
            result = max(result, max_prod);
        }
        return result;
    }
};

// Test
#include <iostream>
int main() {
    Solution sol;
    vector<int> v1 = {2,3,-2,4};
    vector<int> v2 = {-2,0,-1};
    cout << sol.maxProduct(v1) << endl;  // 6
    cout << sol.maxProduct(v2) << endl;  // 0
    return 0;
}
