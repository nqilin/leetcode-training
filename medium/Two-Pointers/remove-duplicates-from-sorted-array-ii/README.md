# [LeetCode 80 - Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)
> Difficulty: Medium | Tags: Array, Two Pointers

## Problem Description
Given a sorted array, remove duplicates in-place such that each element appears at most twice. Return the new length.

## Examples
- Input: nums = [1,1,1,2,2,3]
- Output: 5

## Solution Ideas
1. Use slow pointer to store valid elements.
2. Allow at most two occurrences of each element.
3. Compare current element with the one at slow-2 to avoid third duplicate.

## Code Files
- [Python Solution](sslocal://flow/file_open?url=remove_duplicates.py&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [C++ Solution](sslocal://flow/file_open?url=remove_duplicates.cpp&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## Key Points
- Classic slow-fast two pointers for deduplication
- In-place modification with constant space

## Training Log
- Completed Time: 2026-04-10
- Difficulty Evaluation: ⭐⭐
- Notes: Standard two-pointer deduplication practice
