#include <vector>
#include <algorithm> // For max() function
using namespace std;

/**
 * Find the contiguous subarray with the largest sum (Kadane's Algorithm)
 * @param nums: vector<int> - Input integer array (can contain negative numbers)
 * @return: int - Maximum sum of contiguous subarray
 * Time Complexity: O(n) - Traverse the array once
 * Space Complexity: O(1) - Constant extra space (optimized Kadane's Algorithm)
 */
int maxSubArray(vector<int>& nums) {
    // Current maximum sum of subarray ending at current position
    int current_max = nums[0];
    // Global maximum sum of all subarrays
    int global_max = nums[0];
    
    // Traverse from the second element
    for (int i = 1; i < nums.size(); i++) {
        // Key logic: either start new subarray with current num, or extend previous subarray
        current_max = max(nums[i], current_max + nums[i]);
        // Update global max if current max is larger
        global_max = max(global_max, current_max);
    }
    
    return global_max;
}

// Test case for verification
#include <iostream>
int main() {
    vector<vector<int>> test_cases = {
        {-2,1,-3,4,-1,2,1,-5,4},  // Expected: 6
        {1},                        // Expected: 1
        {5,4,-1,7,8}               // Expected: 23
    };
    
    for (auto& case_nums : test_cases) {
        cout << "Input: [";
        for (int i = 0; i < case_nums.size(); i++) {
            cout << case_nums[i];
            if (i != case_nums.size() - 1) cout << ",";
        }
        cout << "] → Max subarray sum: " << maxSubArray(case_nums) << endl;
    }
    return 0;
}
