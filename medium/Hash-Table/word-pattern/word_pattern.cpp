#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        /*
         * Determine if s follows the same pattern.
         * Approach: Bidirectional hash map
         * Time Complexity: O(n)
         * Space Complexity: O(k)
         */
        vector<string> words = split(s);
        if (pattern.size() != words.size())
            return false;

        unordered_map<char, string> c2w;
        unordered_map<string, char> w2c;

        for (int i = 0; i < pattern.size(); ++i) {
            char c = pattern[i];
            string w = words[i];

            if (c2w.count(c) && c2w[c] != w) return false;
            if (w2c.count(w) && w2c[w] != c) return false;

            c2w[c] = w;
            w2c[w] = c;
        }

        return true;
    }

private:
    vector<string> split(string& s) {
        vector<string> res;
        stringstream ss(s);
        string word;
        while (ss >> word) res.push_back(word);
        return res;
    }
};
