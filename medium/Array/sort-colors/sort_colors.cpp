#include <vector>
using namespace std;

/**
 * Sort an array with 0, 1, 2 in-place (Dutch National Flag Problem)
 * @param nums: vector<int> - Input array containing only 0, 1, 2
 * @return: void - Modify nums in-place instead of returning
 * Time Complexity: O(n) - Traverse the array once (one-pass solution)
 * Space Complexity: O(1) - Constant extra space (in-place sorting)
 */
void sortColors(vector<int>& nums) {
    // Three pointers:
    // left: right boundary of 0s (all elements before left are 0)
    // current: current element to check
    // right: left boundary of 2s (all elements after right are 2)
    int left = 0;
    int current = 0;
    int right = nums.size() - 1;
    
    while (current <= right) {
        if (nums[current] == 0) {
            // Swap current with left (put 0 to 0s region)
            swap(nums[left], nums[current]);
            // Move left forward (expand 0s region)
            left++;
            // Move current forward (processed current element)
            current++;
        }
        else if (nums[current] == 1) {
            // 1 is in correct position, move current forward
            current++;
        }
        else { // nums[current] == 2
            // Swap current with right (put 2 to 2s region)
            swap(nums[current], nums[right]);
            // Move right backward (expand 2s region)
            right--;
            // Do NOT move current (swapped element needs to be checked)
        }
    }
}

// Test case for verification
#include <iostream>
int main() {
    vector<vector<int>> test_cases = {
        {2,0,2,1,1,0},  // Expected: [0,0,1,1,2,2]
        {2,0,1},         // Expected: [0,1,2]
        {0}              // Expected: [0]
    };
    
    for (auto& case_nums : test_cases) {
        sortColors(case_nums);
        cout << "Sorted array: [";
        for (int i = 0; i < case_nums.size(); i++) {
            cout << case_nums[i];
            if (i != case_nums.size() - 1) cout << ",";
        }
        cout << "]" << endl;
    }
    return 0;
}
