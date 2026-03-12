#include <string>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";
        int n = s.size();
        int start = 0, end = 0;

        auto expand = [&](int left, int right) -> int {
            while (left >= 0 && right < n && s[left] == s[right]) {
                left--;
                right++;
            }
            return right - left - 1;
        };

        for (int i = 0; i < n; ++i) {
            int len1 = expand(i, i);
            int len2 = expand(i, i+1);
            int max_len = max(len1, len2);
            if (max_len > end - start) {
                start = i - (max_len - 1) / 2;
                end = i + max_len / 2;
            }
        }

        return s.substr(start, end - start + 1);
    }
};

// Test
#include <iostream>
int main() {
    Solution sol;
    cout << sol.longestPalindrome("babad") << endl;
    cout << sol.longestPalindrome("cbbd") << endl;
    return 0;
}
