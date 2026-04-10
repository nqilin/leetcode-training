# [LeetCode 16 - 3Sum Closest](https://leetcode.com/problems/3sum-closest/)
> Difficulty: Medium | Tags: Array, Two Pointers, Sorting

## Problem Description
Given an array and target, find three integers whose sum is closest to target. Return the sum.

## Examples
- Input: nums = [-1,2,1,-4], target = 1
- Output: 2

## Solution Ideas
1. Sort the array to apply two-pointer technique.
2. Fix one element, use left and right pointers to find best pair.
3. Track the sum with minimal difference to target.

## Code Files
- [Python Solution](sslocal://flow/file_open?url=three_sum_closest.py&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [C++ Solution](sslocal://flow/file_open?url=three_sum_closest.cpp&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)

## Complexity Analysis
- Time Complexity: O(n^2)
- Space Complexity: O(log n)

## Key Points
- Extension of 3Sum using two pointers
- Early return when exact match is found

## Training Log
- Completed Time: 2026-04-10
- Difficulty Evaluation: ⭐⭐
- Notes: Two-pointer closest sum search practice
