# [LeetCode 141 - Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
> Difficulty: Easy | Tags: Linked List, Two Pointers

## 🎯 Problem Description
Given head, check if the linked list has a cycle.

## Examples
- Input: head = [3,2,0,-4], pos = 1
- Output: true

## 💡 Solution Ideas
- Use **fast & slow pointers**
- Fast moves 2 steps, slow moves 1 step
- If they meet → cycle exists
- If fast reaches null → no cycle

## 📁 Code Files
- [Python Solution](has_cycle.py)
- [C++ Solution](has_cycle.cpp)

## ⚡ Complexity
- Time: O(n)
- Space: O(1)

## 📝 Training Log
- Completed Time: 2026-03-21
- Difficulty Evaluation: ⭐
- Notes: Mastered Floyd cycle detection algorithm.
