# [LeetCode 328 - Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)
> Difficulty: Medium | Tags: Linked List

## 🎯 Problem Description
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

## Examples
- Input: 1 -> 2 -> 3 -> 4 -> 5
- Output: 1 -> 3 -> 5 -> 2 -> 4

## 💡 Solution Ideas
- Use two pointers: odd and even.
- Connect odd nodes together, even nodes together.
- Finally link odd list tail to even list head.

## 📁 Code Files
- [Python Solution](odd_even_list.py)
- [C++ Solution](odd_even_list.cpp)

## ⚡ Complexity
- Time: O(n)
- Space: O(1)

## 📝 Training Log
- Completed Time: 2026-03-24
- Difficulty Evaluation: ⭐⭐
- Notes: Mastered linked list segmentation with two pointers.
