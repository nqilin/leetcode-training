#include <string>
#include <vector>
using namespace std;

/**
 * Find the first occurrence of needle in haystack (return starting index)
 * Return -1 if needle is not part of haystack
 * Provide both brute-force and KMP solutions
 * @param haystack: string - Source string
 * @param needle: string - Pattern string to find
 * @return: int - Starting index of first occurrence, or -1
 * Brute-force Time: O(m*n) (m=haystack length, n=needle length)
 * KMP Time: O(m+n) (linear time, optimal for string matching)
 * Space (KMP): O(n) (for prefix table)
 */
int strStr(string haystack, string needle) {
    // --------------------------
    // Solution 1: Brute-force (simple, easy to understand)
    // --------------------------
    // int m = haystack.size();
    // int n = needle.size();
    // // Edge case: needle is empty
    // if (n == 0) return 0;
    // // Iterate through haystack (stop at m-n to avoid out of bounds)
    // for (int i = 0; i <= m - n; i++) {
    //     bool match = true;
    //     for (int j = 0; j < n; j++) {
    //         if (haystack[i+j] != needle[j]) {
    //             match = false;
    //             break;
    //         }
    //     }
    //     if (match) return i;
    // }
    // // Needle not found
    // return -1;

    // --------------------------
    // Solution 2: KMP Algorithm (optimal, linear time)
    // --------------------------
    vector<int> buildPrefixTable(string pattern) {
        int n = pattern.size();
        vector<int> prefix(n, 0);
        // j: length of the previous longest prefix suffix
        int j = 0;
        for (int i = 1; i < n; i++) {
            // Backtrack j until pattern[i] == pattern[j] or j == 0
            while (j > 0 && pattern[i] != pattern[j]) {
                j = prefix[j-1];
            }
            // If match, increment j and set prefix[i]
            if (pattern[i] == pattern[j]) {
                j++;
                prefix[i] = j;
            }
        }
        return prefix;
    }

    int m = haystack.size();
    int n = needle.size();
    // Edge cases
    if (n == 0) return 0;
    if (m < n) return -1;

    // Build prefix table for needle
    vector<int> prefix = buildPrefixTable(needle);
    int j = 0;  // Pointer for needle

    for (int i = 0; i < m; i++) {
        // Backtrack j using prefix table if mismatch
        while (j > 0 && haystack[i] != needle[j]) {
            j = prefix[j-1];
        }
        // If match, increment j
        if (haystack[i] == needle[j]) {
            j++;
        }
        // If j reaches len(needle), found full match
        if (j == n) {
            return i - n + 1;
        }
    }

    // Needle not found
    return -1;
}

// Test case for verification
#include <iostream>
int main() {
    pair<string, string> test_cases[] = {
        {"sadbutsad", "sad"},   // Expected: 0
        {"leetcode", "leeto"},  // Expected: -1
        {"mississippi", "issip"}// Expected: 4
    };

    for (auto& test : test_cases) {
        string haystack = test.first;
        string needle = test.second;
        cout << "haystack='" << haystack << "', needle='" << needle 
             << "' → Index: " << strStr(haystack, needle) << endl;
    }

    return 0;
}
