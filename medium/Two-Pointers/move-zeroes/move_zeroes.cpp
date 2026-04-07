#include <vector>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        /*
         * Move all zeros to the end while maintaining order.
         * Approach: Slow & Fast Two Pointers
         * Time Complexity: O(n)
         * Space Complexity: O(1)
         */
        int slow = 0;
        // Fast pointer collect non-zero values
        for(int fast = 0; fast < nums.size(); fast++){
            if(nums[fast] != 0){
                nums[slow++] = nums[fast];
            }
        }
        // Fill zeros at the end
        for(int i = slow; i < nums.size(); i++){
            nums[i] = 0;
        }
    }
};
