#include <vector>
using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        /*
         * Reverse char array in-place with two pointers.
         * Approach: Left Right Two Pointers Swap
         * Time Complexity: O(n)
         * Space Complexity: O(1)
         */
        int left = 0;
        int right = s.size() - 1;

        // Swap characters from both sides to center
        while(left < right){
            swap(s[left], s[right]);
            left++;
            right--;
        }
    }
};
