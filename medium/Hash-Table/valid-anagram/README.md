# [LeetCode 242 - Valid Anagram](https://leetcode.com/problems/valid-anagram/)
> Difficulty: Easy | Tags: Hash Table, String, Sorting

## 🎯 Problem Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

## Examples
- Input: s = "anagram", t = "nagaram"
- Output: true

- Input: s = "rat", t = "car"
- Output: false

## 💡 Solution Ideas
1. Check if lengths are equal first.
2. Use a hash map to count character frequencies in `s`.
3. Decrement frequencies using characters in `t`.
4. If any count becomes negative, return false.

## 📁 Code Files
- [Python Solution](is_anagram.py)
- [C++ Solution](is_anagram.cpp)

## ⚡ Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1) (fixed number of lowercase letters)

## 📌 Key Points
- Frequency counting with hash table
- Early return for length mismatch and negative count

## 📝 Training Log
- Completed Time: 2026-04-01
- Difficulty Evaluation: ⭐
- Notes: Basic anagram validation using frequency hash map.
