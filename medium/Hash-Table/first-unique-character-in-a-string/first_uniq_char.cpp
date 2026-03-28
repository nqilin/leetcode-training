#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        /*
         * Find the first non-repeating character and return its index.
         * Approach: Hash map for frequency counting
         * Time Complexity: O(n)
         * Space Complexity: O(1)
         */
        unordered_map<char, int> count;

        // Count each character
        for (char c : s) {
            count[c]++;
        }

        // Find first unique one
        for (int i = 0; i < s.size(); ++i) {
            if (count[s[i]] == 1) {
                return i;
            }
        }

        return -1;
    }
};
