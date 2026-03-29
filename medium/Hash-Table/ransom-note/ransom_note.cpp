#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        /*
         * Check if ransomNote can be built from magazine characters.
         * Approach: Hash map frequency count
         * Time Complexity: O(m + n)
         * Space Complexity: O(1)
         */
        unordered_map<char, int> count;

        // Count characters in magazine
        for (char c : magazine) {
            count[c]++;
        }

        // Verify ransomNote
        for (char c : ransomNote) {
            if (count[c] == 0) {
                return false;
            }
            count[c]--;
        }

        return true;
    }
};
