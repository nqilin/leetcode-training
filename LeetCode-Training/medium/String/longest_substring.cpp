#include <string>
#include <unordered_map>
using namespace std;

/**
 * Find the length of the longest substring without repeating characters
 * @param s: string - Input string
 * @return: int - Length of the longest substring without repeating characters
 * Time Complexity: O(n) - Traverse the string once (each character visited at most twice)
 * Space Complexity: O(min(m, n)) - m is the size of character set (e.g., 128 for ASCII)
 */
int lengthOfLongestSubstring(string s) {
    // Hash map to store the last index of each character
    unordered_map<char, int> char_index;
    // Left pointer of sliding window, max length of valid substring
    int left = 0;
    int max_length = 0;
    
    // Right pointer of sliding window (iterate through each character)
    for (int right = 0; right < s.size(); right++) {
        char current_char = s[right];
        // If character exists in map and its index >= left (in current window)
        if (char_index.find(current_char) != char_index.end() && char_index[current_char] >= left) {
            // Move left pointer to the right of the repeated character
            left = char_index[current_char] + 1;
        }
        
        // Update the last index of current character
        char_index[current_char] = right;
        // Calculate current window length and update max length
        int current_length = right - left + 1;
        if (current_length > max_length) {
            max_length = current_length;
        }
    }
    
    return max_length;
}

// Test case for verification
int main() {
    string test_cases[] = {"abcabcbb", "bbbbb", "pwwkew"};
    // Expected outputs: 3, 1, 3
    for (string s : test_cases) {
        printf("Input: '%s' → Longest length: %d\n", s.c_str(), lengthOfLongestSubstring(s));
    }
    return 0;
}
