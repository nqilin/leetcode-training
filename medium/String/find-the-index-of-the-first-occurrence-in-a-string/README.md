# [LeetCode 28 - Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
> Difficulty: Medium | Tags: String, Two Pointers, String Matching, KMP

## 🎯 Problem Description
Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.
- Clarification: What should we return when `needle` is an empty string? According to the problem statement, return 0 (consistent with C's strstr() and Java's indexOf()).

Examples:
1. Input: haystack = "sadbutsad", needle = "sad" → Output: 0
   Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0.
2. Input: haystack = "leetcode", needle = "leeto" → Output: -1
3. Input: haystack = "mississippi", needle = "issip" → Output: 4

## 💡 Solution Ideas
### 1. Brute-force Solution (Basic)
- Core Idea: Check every possible starting position in haystack for needle match
- Step-by-Step:
  1. Iterate haystack from 0 to len(haystack)-len(needle) (avoid out of bounds)
  2. For each position i, check if haystack[i:i+n] equals needle (n=len(needle))
  3. Return i if match found, else return -1
- Pros: Simple to implement, easy to understand
- Cons: O(m*n) time complexity (slow for large strings)

### 2. KMP Algorithm (Optimal)
- Core Idea: Use prefix table (Longest Prefix Suffix, LPS) to avoid rechecking characters
- Key Concepts:
  - Prefix: Proper prefix (excludes full string) of a substring
  - Suffix: Proper suffix (excludes full string) of a substring
  - LPS Table: For each position in needle, store length of longest prefix that is also suffix
- Step-by-Step:
  1. Build LPS table for needle (O(n) time)
  2. Use two pointers to traverse haystack (i) and needle (j):
     - If match: increment both pointers
     - If mismatch: backtrack j using LPS table (no need to reset i)
     - If j reaches len(needle): return i-n+1 (starting index)
- Pros: O(m+n) linear time (optimal for string matching)
- Cons: Slightly more complex to implement

## 📁 Code Files
- [Python Solution](str_str.py)
- [C++ Solution](str_str.cpp)

## ⚡ Complexity Analysis
| Solution   | Time Complexity | Space Complexity |
|------------|-----------------|------------------|
| Brute-force| O(m*n)          | O(1)             |
| KMP        | O(m+n)          | O(n)             |
- m = length of haystack, n = length of needle

## 📌 Problem-Solving Tips
1. Brute-force Optimization: Stop iteration at m-n (avoid unnecessary checks)
2. KMP Key Points:
   - LPS Table Construction: Backtrack j to prefix[j-1] when mismatch occurs
   - Pointer Backtracking: Only backtrack j (needle pointer), not i (haystack pointer)
3. Edge Cases to Handle:
   - Needle is empty string → return 0
   - Haystack length < needle length → return -1
   - Needle equals haystack → return 0
4. Real-World Application: KMP is used in text editors, search engines, and bioinformatics (DNA sequence matching)

## 📝 Training Log
- Completed Time: 2026-03-11
- Difficulty Evaluation: ⭐⭐⭐ (1-5 stars)
- Notes: Mastered brute-force string matching; learned KMP algorithm (core of efficient string matching); understood LPS table construction and its role in avoiding rechecking
