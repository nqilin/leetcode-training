#include <vector>
#include <algorithm> // For min() function
using namespace std;

/**
 * Calculate the maximum area of water that can be contained by two lines
 * @param height: vector<int> - Array of non-negative integers representing height of lines
 * @return: int - Maximum area of water
 * Time Complexity: O(n) - Traverse the array once
 * Space Complexity: O(1) - Constant extra space
 */
int maxArea(vector<int>& height) {
    // Initialize two pointers and max area
    int left = 0;
    int right = height.size() - 1;
    int max_area = 0;
    
    // Two pointers traverse towards each other
    while (left < right) {
        // Calculate current area: min height * width
        int current_width = right - left;
        int current_height = min(height[left], height[right]);
        int current_area = current_height * current_width;
        
        // Update max area if current area is larger
        if (current_area > max_area) {
            max_area = current_area;
        }
        
        // Move the pointer with smaller height (key logic)
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return max_area;
}

// Test case for verification
int main() {
    vector<int> test_height = {1,8,6,2,5,4,8,3,7};
    // Expected output: 49
    printf("Max area: %d\n", maxArea(test_height));
    return 0;
}
