# [LeetCode 142 - Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
> Difficulty: Medium | Tags: Linked List, Two Pointers

## 🎯 Problem Description
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

## Examples
- Input: head = [3,2,0,-4], pos = 1
- Output: tail connects to node index 1

## 💡 Solution Ideas
1. Use **fast & slow pointers** to determine if a cycle exists.
2. Once they meet, move the slow pointer back to the head.
3. Move both pointers **one step at a time**; the meeting point is the cycle entrance.

## 📁 Code Files
- [Python Solution](detect_cycle.py)
- [C++ Solution](detect_cycle.cpp)

## ⚡ Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## 📌 Key Points
- Floyd’s Cycle-Finding Algorithm
- First meeting: confirm cycle
- Second meeting: find cycle entrance

## 📝 Training Log
- Completed Time: 2026-03-25
- Difficulty Evaluation: ⭐⭐⭐
- Notes: Mastered finding linked list cycle entrance with two pointers.
