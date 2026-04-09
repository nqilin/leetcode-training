# [LeetCode 18 - 4Sum](https://leetcode.com/problems/4sum/)
> Difficulty: Medium | Tags: Array, Two Pointers, Sorting

## Problem Description
Given an array nums and target, return all unique quadruplets [a, b, c, d] such that a + b + c + d = target.

## Examples
- Input: nums = [1,0,-1,0,-2,2], target = 0
- Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

## Solution Ideas
1. Sort the array to enable two-pointer technique.
2. Use two nested loops for first two elements.
3. Use left and right pointers for the remaining two elements.
4. Skip duplicates to avoid repeated quadruplets.

## Code Files
- [Python Solution](four_sum.py)
- [C++ Solution](four_sum.cpp)

## Complexity Analysis
- Time Complexity: O(n^3)
- Space Complexity: O(log n)

## Key Points
- Extension of 3Sum using two pointers
- Critical duplicate skipping logic

## Training Log
- Completed Time: 2026-04-09
- Difficulty Evaluation: ⭐⭐⭐
- Notes: Advanced two-pointer problem for four elements sum
