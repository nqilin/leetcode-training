# [LeetCode 344 - Reverse String](https://leetcode.com/problems/reverse-string/)
> Difficulty: Easy | Tags: Two Pointers, String

## 🎯 Problem Description
Write a function that reverses a string in-place.
The input string is given as an array of characters s.

## Examples
- Input: s = ["h","e","l","l","o"]
- Output: ["o","l","l","e","h"]

## 💡 Solution Ideas
1. Set left pointer at start, right pointer at end.
2. Swap characters at left and right position.
3. Move two pointers toward the center until they meet.
4. All operations are done in-place without extra space.

## 📁 Code Files
- [Python Solution](sslocal://flow/file_open?url=reverse_string.py&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [C++ Solution](sslocal://flow/file_open?url=reverse_string.cpp&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)

## ⚡ Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## 📌 Key Points
- Classic two-pointer in-place swap
- No additional memory usage

## 📝 Training Log
- Completed Time: 2026-04-06
- Difficulty Evaluation: ⭐
- Notes: Basic two-pointer reverse operation practice.
