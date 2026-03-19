# [LeetCode 128 - Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
> Difficulty: Medium | Tags: Array, Hash Table

## 🎯 Problem Description
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
**Algorithm must run in O(n) time.**

## Examples
- Input: nums = [100,4,200,1,3,2]
- Output: 4
- Explanation: The longest consecutive sequence is [1,2,3,4].

## 💡 Solution Ideas
1. Use a **hash set** for O(1) lookups.
2. Only start counting from a **sequence beginning** (num - 1 not in set).
3. Expand to the right as long as num+1 exists.
4. Keep track of maximum length.

## 📁 Code Files
- [Python Solution](longest_consecutive.py)
- [C++ Solution](longest_consecutive.cpp)

## ⚡ Complexity
- Time: O(n)
- Space: O(n)

## 📝 Training Log
- Completed Time: 2026-03-19
- Difficulty Evaluation: ⭐⭐⭐
- Notes: Mastered O(n) sequence finding using hash set.
