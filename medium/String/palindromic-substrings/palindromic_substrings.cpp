#include <string>
using namespace std;

class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        int count = 0;

        auto expand = [&](int l, int r) {
            while (l >= 0 && r < n && s[l] == s[r]) {
                count++;
                l--;
                r++;
            }
        };

        for (int i = 0; i < n; ++i) {
            expand(i, i);
            expand(i, i+1);
        }
        return count;
    }
};

// Test
#include <iostream>
int main() {
    Solution sol;
    cout << sol.countSubstrings("abc") << endl;
    cout << sol.countSubstrings("aaa") << endl;
    return 0;
}
