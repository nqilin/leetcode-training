# [LeetCode 3 - Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
> Difficulty: Medium | Tags: String, Hash Table, Sliding Window

## 🎯 Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.
- A substring is a contiguous non-empty sequence of characters within a string.

Examples:
1. Input: s = "abcabcbb" → Output: 3 (Explanation: The answer is "abc", with length 3)
2. Input: s = "bbbbb" → Output: 1 (Explanation: The answer is "b", with length 1)
3. Input: s = "pwwkew" → Output: 3 (Explanation: The answer is "wke", with length 3; "pwke" is a subsequence, not a substring)

## 💡 Solution Ideas
1. Core Idea: Use **sliding window + hash table** to track the longest valid substring (O(n) time complexity)
2. Step-by-Step Explanation:
   - Use two pointers (left/right) to represent the current sliding window (valid substring without duplicates)
   - Use a hash map to store the last index of each character (to quickly find repeated characters)
   - Expand the window with right pointer: for each character, check if it's in the current window
   - If repeated: move left pointer to the right of the last occurrence of the repeated character
   - Update the hash map and calculate the current window length, keep track of the maximum length
3. Edge Cases:
   - Empty string: return 0
   - Single character string: return 1
   - All unique characters (e.g., "abcd"): return length of string
   - All repeated characters (e.g., "aaaaa"): return 1

## 📁 Code Files
- [Python Solution](longest_substring.py)
- [C++ Solution](longest_substring.cpp)

## ⚡ Complexity Analysis
- **Time Complexity (TC)**: O(n) 
  - Each character is visited at most twice (once by right pointer, once by left pointer)
  - Hash table operations (insert/find) are O(1) average case
- **Space Complexity (SC)**: O(min(m, n))
  - m: size of the character set (e.g., 128 for ASCII, 256 for extended ASCII)
  - n: length of the input string
  - The hash map will store at most min(m, n) characters (no more than the character set size)

## 📌 Problem-Solving Tips
1. Key Optimization: Sliding window avoids brute force O(n²) solution (check all substrings)
2. Hash Table Role: Replaces O(n) duplicate check with O(1) lookup (critical for O(n) time)
3. Common Mistake: Forgetting to check `char_index[char] >= left` (only move left if the repeated character is in the current window)
4. Alternative Approach: Can use an array (size 128) instead of hash map for faster access (since characters are ASCII)
5. Extension: This sliding window pattern applies to many substring problems (e.g., longest substring with at most k distinct characters)

## 📝 Training Log
- Completed Time: 2026-03-02 
- Difficulty Evaluation: ⭐⭐⭐ (1-5 stars)
- Notes: Mastered sliding window technique for string problems; need to practice different window adjustment logic
