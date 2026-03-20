# [LeetCode 206 - Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
> Difficulty: Easy | Tags: Linked List

## 🎯 Problem Description
Given the head of a singly linked list, reverse the list, and return the reversed list.

## Examples
- Input: 1 -> 2 -> 3 -> 4 -> 5
- Output: 5 -> 4 -> 3 -> 2 -> 1

## 💡 Solution Ideas
- Use **three pointers**: prev, curr, next.
- Iterate and flip the `next` pointer of each node.
- Finally, prev becomes new head.

## 📁 Code Files
- [Python Solution](reverse_list.py)
- [C++ Solution](reverse_list.cpp)

## ⚡ Complexity
- Time: O(n)
- Space: O(1)

## 📝 Training Log
- Completed Time: 2026-03-20
- Difficulty Evaluation: ⭐
- Notes: Mastered basic linked list reversal with iterative approach.
