# [LeetCode 56 - Merge Intervals](https://leetcode.com/problems/merge-intervals/)
> Difficulty: Medium | Tags: Array, Sorting

## 🎯 Problem Description
Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals.

## Examples
- Input: [[1,3],[2,6],[8,10],[15,18]]
- Output: [[1,6],[8,10],[15,18]]

## 💡 Solution Ideas
1. Sort intervals by their start value.
2. Iterate and merge:
   - If current interval overlaps with last merged interval → update end.
   - Else → add as new interval.

## 📁 Code Files
- [Python Solution](merge_intervals.py)
- [C++ Solution](merge_intervals.cpp)

## ⚡ Complexity
- Time: O(n log n) (sorting)
- Space: O(1) / O(n)

## 📝 Training Log
- Completed Time: 2026-03-17
- Difficulty Evaluation: ⭐⭐
- Notes: Mastered interval merging pattern.
