#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        /*
         * Check if t is an anagram of s.
         * Approach: Hash map frequency count
         * Time Complexity: O(n)
         * Space Complexity: O(1)
         */
        if (s.size() != t.size())
            return false;

        unordered_map<char, int> cnt;

        for (char c : s)
            cnt[c]++;

        for (char c : t) {
            if (--cnt[c] < 0)
                return false;
        }

        return true;
    }
};
