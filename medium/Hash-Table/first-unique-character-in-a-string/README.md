# [LeetCode 387 - First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)
> Difficulty: Easy | Tags: Hash Table, String

## 🎯 Problem Description
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

## Examples
- Input: s = "leetcode"
- Output: 0

- Input: s = "loveleetcode"
- Output: 2

## 💡 Solution Ideas
1. Traverse the string and use a hash map to record character frequencies.
2. Traverse the string again to find the first character with frequency equal to 1.
3. Since there are only lowercase letters, space complexity is O(1).

## 📁 Code Files
- [Python Solution](first_uniq_char.py)
- [C++ Solution](first_uniq_char.cpp)

## ⚡ Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## 📌 Key Points
- Two-pass traversal with hash counting
- Constant extra space due to limited character set

## 📝 Training Log
- Completed Time: 2026-03-28
- Difficulty Evaluation: ⭐
- Notes: Practiced basic frequency counting using hash table.
