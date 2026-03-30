#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        /*
         * Check if two strings are isomorphic.
         * Approach: Two hash maps for bidirectional character mapping
         * Time Complexity: O(n)
         * Space Complexity: O(1)
         */
        unordered_map<char, char> s2t;
        unordered_map<char, char> t2s;

        for (int i = 0; i < s.size(); ++i) {
            char c1 = s[i];
            char c2 = t[i];

            if (s2t.count(c1) && s2t[c1] != c2)
                return false;
            if (t2s.count(c2) && t2s[c2] != c1)
                return false;

            s2t[c1] = c2;
            t2s[c2] = c1;
        }

        return true;
    }
};
