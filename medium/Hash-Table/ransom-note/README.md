# [LeetCode 383 - Ransom Note](https://leetcode.com/problems/ransom-note/)
> Difficulty: Easy | Tags: Hash Table, String

## 🎯 Problem Description
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed from `magazine`, and `false` otherwise.

Each character in `magazine` can only be used once in `ransomNote`.

## Examples
- Input: ransomNote = "a", magazine = "b"
- Output: false

- Input: ransomNote = "aa", magazine = "aab"
- Output: true

## 💡 Solution Ideas
1. Count character frequency in `magazine` using a hash map.
2. Traverse `ransomNote` and check if each character exists with sufficient count.
3. Return false immediately if any character is missing or insufficient.

## 📁 Code Files
- [Python Solution](ransom_note.py)
- [C++ Solution](ransom_note.cpp)

## ⚡ Complexity Analysis
- Time Complexity: O(m + n)
- Space Complexity: O(1) (only lowercase letters)

## 📌 Key Points
- Frequency counting with hash table
- Early return for efficiency

## 📝 Training Log
- Completed Time: 2026-03-29
- Difficulty Evaluation: ⭐
- Notes: Practiced hash table usage for character availability checking.
