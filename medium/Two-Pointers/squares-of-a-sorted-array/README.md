# [LeetCode 977 - Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
> Difficulty: Easy | Tags: Array, Two Pointers, Sorting

## Problem Description
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

## Examples
- Input: nums = [-4,-1,0,3,10]
- Output: [0,1,9,16,100]

## Solution Ideas
1. Use two pointers starting from the leftmost and rightmost position.
2. Compare the square values of two ends.
3. Place the larger square at the current tail of result array.
4. Move the corresponding pointer inward until finished.

## Code Files
- [Python Solution](sslocal://flow/file_open?url=sorted_squares.py&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [C++ Solution](sslocal://flow/file_open?url=sorted_squares.cpp&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(n)

## Key Points
- Two pointers pick larger square from both ends
- Avoid full sorting to optimize time performance

## Training Log
- Completed Time: 2026-04-08
- Difficulty Evaluation: ⭐
- Notes: Classic two pointers for sorted negative-positive array
