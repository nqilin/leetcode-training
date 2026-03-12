# [LeetCode 5 - Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
> Difficulty: Medium | Tags: String, Two Pointers, Dynamic Programming

## 🎯 Problem Description
Given a string s, return the longest palindromic substring in s.

## 💡 Solution Ideas
- Use **Expand Around Center** (two pointers).
- A palindrome can be:
  1. Odd length: center is one character.
  2. Even length: center is between two characters.
- For each center, expand as far as possible while characters are equal.
- Keep track of the longest palindrome’s start and end indices.

## 📁 Code Files
- [Python Solution](longest_palindrome.py)
- [C++ Solution](longest_palindrome.cpp)

## ⚡ Complexity
- Time: O(n²)
- Space: O(1)

## 📝 Training Log
- Completed Time: 2026-03-12
- Difficulty Evaluation: ⭐⭐⭐
- Notes: Mastered expand-around-center for palindrome problems.
