# [LeetCode 125 - Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
> Difficulty: Easy | Tags: Two Pointers, String

## 🎯 Problem Description
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

## Examples
- Input: s = "A man, a plan, a canal: Panama"
- Output: true

## 💡 Solution Ideas
- Use left and right two pointers moving towards center.
- Skip non-alphanumeric characters.
- Compare characters in lowercase.
- Return false if any mismatch found.

## 📁 Code Files
- [Python Solution](valid_palindrome.py)
- [C++ Solution](valid_palindrome.cpp)

## ⚡ Complexity
- Time: O(n)
- Space: O(1)

## 📝 Training Log
- Completed Time: 2026-04-04
- Difficulty Evaluation: ⭐
- Notes: Classic two pointers palindrome check problem.
