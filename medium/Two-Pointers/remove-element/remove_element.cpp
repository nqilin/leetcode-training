#include <vector>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        /*
         * Remove all target values in-place, return new length.
         * Approach: Slow & Fast Two Pointers
         * Time Complexity: O(n)
         * Space Complexity: O(1)
         */
        // Slow pointer stores valid element index
        int slow = 0;
        // Fast pointer iterates the whole array
        for(int fast = 0; fast < nums.size(); fast++){
            // Save element when it is not equal to target
            if(nums[fast] != val){
                nums[slow++] = nums[fast];
            }
        }
        return slow;
    }
};
