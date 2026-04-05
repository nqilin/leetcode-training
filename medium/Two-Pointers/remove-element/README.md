# [LeetCode 27 - Remove Element](https://leetcode.com/problems/remove-element/)
> Difficulty: Easy | Tags: Array, Two Pointers

## 🎯 Problem Description
Given an array nums and an integer val, remove all occurrences of val in-place and return the new length.
Do not use extra array space, modify the input array directly.

## Examples
- Input: nums = [3,2,2,3], val = 3
- Output: 2, modified nums = [2,2]

## 💡 Solution Ideas
1. Use slow pointer to save valid elements.
2. Use fast pointer to traverse all elements.
3. Overwrite slow position with fast element if not target.
4. Final slow value is the new array length.

## 📁 Code Files
- [Python Solution](sslocal://flow/file_open?url=remove_element.py&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [C++ Solution](sslocal://flow/file_open?url=remove_element.cpp&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)

## ⚡ Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## 📌 Key Points
- Classic slow-fast two pointers in-place operation
- No additional memory allocation

## 📝 Training Log
- Completed Time: 2026-04-05
- Difficulty Evaluation: ⭐
- Notes: Basic practice for in-place filtering with two pointers.
