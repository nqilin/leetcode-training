#include <vector>
#include <algorithm> // For sort() function
using namespace std;

/**
 * Find all unique triplets in the array which gives the sum of zero
 * @param nums: vector<int> - Input integer array
 * @return: vector<vector<int>> - List of unique triplets [a,b,c] where a+b+c=0
 * Time Complexity: O(n²) - Sort O(n log n) + two pointers traverse O(n²)
 * Space Complexity: O(log n) ~ O(n) - Depends on sorting algorithm space
 */
vector<vector<int>> threeSum(vector<int>& nums) {
    // Result list to store unique triplets
    vector<vector<int>> result;
    // Sort the array (key for two pointers and duplicate removal)
    sort(nums.begin(), nums.end());
    int n = nums.size();
    
    // Iterate through each element as the first number of triplet
    for (int i = 0; i < n; i++) {
        // Skip duplicate first element to avoid duplicate triplets
        if (i > 0 && nums[i] == nums[i-1]) {
            continue;
        }
        
        // Target sum for the other two numbers
        int target = -nums[i];
        // Two pointers: left starts after i, right at the end
        int left = i + 1;
        int right = n - 1;
        
        while (left < right) {
            int current_sum = nums[left] + nums[right];
            
            if (current_sum == target) {
                // Found valid triplet, add to result
                result.push_back({nums[i], nums[left], nums[right]});
                
                // Skip duplicate left element
                while (left < right && nums[left] == nums[left+1]) {
                    left++;
                }
                // Skip duplicate right element
                while (left < right && nums[right] == nums[right-1]) {
                    right--;
                }
                
                // Move both pointers to find new combinations
                left++;
                right--;
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
    }
    
    return result;
}

// Test case for verification
int main() {
    vector<int> test_nums = {-1,0,1,2,-1,-4};
    vector<vector<int>> result = threeSum(test_nums);
    
    // Print result (Expected: [[-1,-1,2],[-1,0,1]])
    printf("3Sum result:\n");
    for (auto triplet : result) {
        printf("[%d, %d, %d]\n", triplet[0], triplet[1], triplet[2]);
    }
    return 0;
}
