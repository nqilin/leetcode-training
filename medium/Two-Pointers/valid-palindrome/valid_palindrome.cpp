#include <string>
#include <cctype>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        /*
         * Check if the string is a valid palindrome.
         * Approach: Two Pointers
         * Time: O(n)
         * Space: O(1)
         */
        // Initialize left and right pointers
        int left = 0;
        int right = s.size() - 1;

        while (left < right) {
            // Skip non-alphanumeric characters on left
            while (left < right && !isalnum(s[left])) left++;
            // Skip non-alphanumeric characters on right
            while (left < right && !isalnum(s[right])) right--;

            // Compare characters in lowercase
            if (tolower(s[left]) != tolower(s[right])) {
                return false;
            }

            // Move pointers towards center
            left++;
            right--;
        }
        return true;
    }
};

// Test
#include <iostream>
int main() {
    Solution sol;
    string s = "A man, a plan, a canal: Panama";
    cout << sol.isPalindrome(s) << endl;
    return 0;
}
