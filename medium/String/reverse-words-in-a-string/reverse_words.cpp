#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        vector<string> words;
        stringstream ss(s);
        string word;
        
        while (ss >> word) {
            words.push_back(word);
        }
        
        reverse(words.begin(), words.end());
        
        string res;
        for (int i = 0; i < words.size(); ++i) {
            if (i > 0) res += " ";
            res += words[i];
        }
        return res;
    }
};

// Test
#include <iostream>
int main() {
    Solution sol;
    cout << sol.reverseWords("the sky is blue") << endl;
    return 0;
}
