# [LeetCode 283 - Move Zeroes](https://leetcode.com/problems/move-zeroes/)
> Difficulty: Easy | Tags: Array, Two Pointers

## 🎯 Problem Description
Given an array nums, move all 0's to the end of it while keeping the relative order of non-zero elements.
Must do in-place without extra array.

## Examples
- Input: nums = [0,1,0,3,12]
- Output: [1,3,12,0,0]

## 💡 Solution Ideas
1. Use a fast pointer to traverse all elements.
2. Use a slow pointer to record positions of non-zero elements.
3. Overwrite non-zero elements to the front of the array.
4. Fill the remaining positions with zeros.

## 📁 Code Files
- [Python Solution](sslocal://flow/file_open?url=move_zeroes.py&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [C++ Solution](sslocal://flow/file_open?url=move_zeroes.cpp&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)

## ⚡ Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## 📌 Key Points
- Classic slow-fast two pointers in-place operation
- Keep relative order of original elements

## 📝 Training Log
- Completed Time: 2026-04-07
- Difficulty Evaluation: ⭐
- Notes: Standard two-pointer in-place rearrangement.
