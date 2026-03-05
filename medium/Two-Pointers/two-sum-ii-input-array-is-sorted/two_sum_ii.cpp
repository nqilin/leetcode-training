#include <vector>
using namespace std;

/**
 * Find two numbers in a sorted array that add up to a target (1-indexed)
 * @param numbers: vector<int> - Sorted non-decreasing integer array
 * @param target: int - Target sum
 * @return: vector<int> - 1-indexed indices of the two numbers (first < second)
 * Time Complexity: O(n) - Traverse the array once with two pointers
 * Space Complexity: O(1) - Constant extra space (no hash map)
 */
vector<int> twoSum(vector<int>& numbers, int target) {
    // Initialize two pointers: left at start, right at end
    int left = 0;
    int right = numbers.size() - 1;
    
    while (left < right) {
        int current_sum = numbers[left] + numbers[right];
        
        if (current_sum == target) {
            // Return 1-indexed indices
            return {left + 1, right + 1};
        }
        else if (current_sum < target) {
            // Need larger sum, move left pointer right
            left++;
        }
        else {
            // Need smaller sum, move right pointer left
            right--;
        }
    }
    
    // Problem guarantees exactly one solution, so no need for default return
    return {};
}

// Test case for verification
#include <iostream>
int main() {
    vector<int> test_numbers = {2,7,11,15};
    int test_target = 9;
    vector<int> result = twoSum(test_numbers, test_target);
    // Expected output: 1 2
    cout << "Indices: " << result[0] << " " << result[1] << endl;
    return 0;
}
