# [LeetCode 205 - Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)
> Difficulty: Easy | Tags: Hash Table, String

## 🎯 Problem Description
Given two strings `s` and `t`, determine if they are isomorphic.

Two strings are isomorphic if the characters in `s` can be replaced to get `t`.
All occurrences of a character must be replaced with another character while preserving the order.
No two characters may map to the same character, but a character may map to itself.

## Examples
- Input: s = "egg", t = "add"
- Output: true

- Input: s = "foo", t = "bar"
- Output: false

## 💡 Solution Ideas
1. Use two hash maps to build **bidirectional character mapping**.
2. Ensure each character maps to exactly one unique character.
3. If any conflict is found during traversal, return false.

## 📁 Code Files
- [Python Solution](is_isomorphic.py)
- [C++ Solution](is_isomorphic.cpp)

## ⚡ Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1) (limited ASCII characters)

## 📌 Key Points
- Bidirectional hash mapping
- Early return on conflict

## 📝 Training Log
- Completed Time: 2026-03-30
- Difficulty Evaluation: ⭐
- Notes: Practiced bidirectional hash mapping for string pattern.
