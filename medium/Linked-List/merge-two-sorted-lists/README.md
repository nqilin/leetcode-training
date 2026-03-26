# [LeetCode 21 - Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
> Difficulty: Easy | Tags: Linked List, Recursion

## 🎯 Problem Description
Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.

## Examples
- Input: list1 = [1,2,4], list2 = [1,3,4]
- Output: [1,1,2,3,4,4]

## 💡 Solution Ideas
1. Use a **dummy node** to build the merged list.
2. Compare nodes from list1 and list2, append the smaller one.
3. Attach the remaining non-empty list at the end.

## 📁 Code Files
- [Python Solution](merge_two_lists.py)
- [C++ Solution](merge_two_lists.cpp)

## ⚡ Complexity Analysis
- Time Complexity: O(n + m)
- Space Complexity: O(1)

## 📌 Key Points
- Dummy node simplifies edge cases
- Iterative approach is efficient and easy to implement

## 📝 Training Log
- Completed Time: 2026-03-26
- Difficulty Evaluation: ⭐
- Notes: Mastered merging two sorted linked lists.
