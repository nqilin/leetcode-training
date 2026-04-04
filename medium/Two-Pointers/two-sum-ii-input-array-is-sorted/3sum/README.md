# [LeetCode 15 - 3Sum](https://leetcode.com/problems/3sum/)
> Difficulty: Medium | Tags: Array, Two Pointers, Sorting

## 🎯 Problem Description
Given an integer array nums, return all unique triplets [a,b,c] such that a+b+c = 0.

## Examples
- Input: nums = [-1,0,1,2,-1,-4]
- Output: [[-1,-1,2],[-1,0,1]]

## 💡 Solution Ideas
1. Sort the whole array first.
2. Fix the first number, use left & right two pointers.
3. Skip duplicate elements to avoid repeated triplets.

## 📁 Code Files
- [Python Solution](sslocal://flow/file_open?url=three_sum.py&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [C++ Solution](sslocal://flow/file_open?url=three_sum.cpp&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)

## ⚡ Complexity Analysis
- Time Complexity: O(n^2)
- Space Complexity: O(log n)

## 📌 Key Points
- Classic two-pointer problem after sorting
- Deduplication logic is critical

## 📝 Training Log
- Completed Time: 2026-04-04
- Difficulty Evaluation: ⭐⭐⭐
- Notes: Mastered core two-pointer triplet search.
