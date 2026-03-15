# [LeetCode 438 - Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
> Difficulty: Medium | Tags: String, Hash Table, Sliding Window

## 🎯 Problem Description
Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`.

## Examples
- Input: s = "cbaebabacd", p = "abc"
- Output: [0,6]

## 💡 Solution Ideas
- Use **sliding window** with fixed length (length of p).
- Use two frequency arrays to compare character counts.
- If counts are equal → current window is an anagram.

## 📁 Code Files
- [Python Solution](find_anagrams.py)
- [C++ Solution](find_anagrams.cpp)

## ⚡ Complexity
- Time: O(n)
- Space: O(1)

## 📝 Training Log
- Completed Time: 2026-03-15
- Difficulty Evaluation: ⭐⭐⭐
- Notes: Mastered sliding window for anagram & substring matching.
