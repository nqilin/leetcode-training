# [LeetCode 290 - Word Pattern](https://leetcode.com/problems/word-pattern/)
> Difficulty: Easy | Tags: Hash Table, String

## 🎯 Problem Description
Given a `pattern` and a string `s`, check if `s` follows the same pattern.

**Follow** means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.

## Examples
- Input: pattern = "abba", s = "dog cat cat dog"
- Output: true

- Input: pattern = "abba", s = "dog cat cat fish"
- Output: false

## 💡 Solution Ideas
1. Split string `s` into words.
2. Use **two hash maps** to ensure bijection:
   - character → word
   - word → character
3. If any conflict is found, return false.

## 📁 Code Files
- [Python Solution](word_pattern.py)
- [C++ Solution](word_pattern.cpp)

## ⚡ Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(k), k is number of unique words/characters

## 📌 Key Points
- Bijection (bidirectional mapping)
- Split string into words
- Early return on conflict

## 📝 Training Log
- Completed Time: 2026-03-31
- Difficulty Evaluation: ⭐
- Notes: Similar to isomorphic strings, applied to word pattern.
