#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int len_s = s.size();
        int len_p = p.size();
        vector<int> res;

        if (len_p > len_s) return res;

        vector<int> count_s(26, 0);
        vector<int> count_p(26, 0);

        for (int i = 0; i < len_p; ++i) {
            count_p[p[i] - 'a']++;
            count_s[s[i] - 'a']++;
        }

        if (count_s == count_p) {
            res.push_back(0);
        }

        for (int i = len_p; i < len_s; ++i) {
            count_s[s[i - len_p] - 'a']--;
            count_s[s[i] - 'a']++;

            if (count_s == count_p) {
                res.push_back(i - len_p + 1);
            }
        }

        return res;
    }
};

// Test
#include <iostream>
int main() {
    Solution sol;
    vector<int> ans = sol.findAnagrams("cbaebabacd", "abc");
    for (int x : ans) cout << x << " ";
    return 0;
}
