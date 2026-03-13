# [LeetCode 647 - Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
> Difficulty: Medium | Tags: String, Two Pointers

## 🎯 Problem Description
Given a string s, return the number of **palindromic substrings** in it.
A substring is a contiguous sequence of characters within the string.
A string is a palindrome if it reads the same forward and backward.

## Examples
- Input: s = "abc" → Output: 3
  Explanation: "a", "b", "c"
- Input: s = "aaa" → Output: 6
  Explanation: "a","a","a","aa","aa","aaa"

## 💡 Solution Ideas
- Use **Expand Around Center** (same as longest palindromic substring).
- Every single character is a palindrome.
- Every pair of equal adjacent characters is a palindrome.
- For each center, expand as long as the substring remains a palindrome.
- Count every valid expansion.

## 📁 Code Files
- [Python Solution](palindromic_substrings.py)
- [C++ Solution](palindromic_substrings.cpp)

## ⚡ Complexity
- Time: O(n²)
- Space: O(1)

## 📌 Key Points
- Two types of centers: odd length (single char) and even length (two chars).
- Each valid expansion = one palindromic substring.
- This is the most efficient and intuitive approach for interviews.

## 📝 Training Log
- Completed Time: 2026-03-13
- Difficulty Evaluation: ⭐⭐⭐
- Notes: Mastered counting palindromes with expand-around-center.
