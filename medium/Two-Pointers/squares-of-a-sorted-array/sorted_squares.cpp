#include <vector>
using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        /*
         * Compute square of each element and return sorted array.
         * Approach: Left Right Two Pointers from both ends
         * Time Complexity: O(n)
         * Space Complexity: O(n)
         */
        int n = nums.size();
        vector<int> res(n);
        int left = 0, right = n - 1, idx = n - 1;
        
        while(left <= right){
            int leftSq = nums[left] * nums[left];
            int rightSq = nums[right] * nums[right];
            if(leftSq > rightSq){
                res[idx--] = leftSq;
                left++;
            }else{
                res[idx--] = rightSq;
                right--;
            }
        }
        return res;
    }
};
