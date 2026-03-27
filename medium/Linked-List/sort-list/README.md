# [LeetCode 148 - Sort List](https://leetcode.com/problems/sort-list/)
> Difficulty: Medium | Tags: Linked List, Merge Sort

## 🎯 Problem Description
Given the head of a linked list, return the list after sorting it in ascending order.
**Requirement: O(n log n) time and constant space.**

## Examples
- Input: head = [4,2,1,3]
- Output: [1,2,3,4]

## 💡 Solution Ideas
1. Use **Merge Sort** for linked list.
2. Find middle with slow & fast pointers.
3. Recursively split and sort.
4. Merge two sorted halves.

## 📁 Code Files
- [Python Solution](sort_list.py)
- [C++ Solution](sort_list.cpp)

## ⚡ Complexity Analysis
- Time Complexity: O(n log n)
- Space Complexity: O(log n)

## 📌 Key Points
- Merge sort is ideal for linked lists.
- No extra array needed; in-place splitting & merging.

## 📝 Training Log
- Completed Time: 2026-03-27
- Difficulty Evaluation: ⭐⭐⭐
- Notes: Mastered merge sort on linked list.
