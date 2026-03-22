# [LeetCode 160 - Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)
> Difficulty: Easy | Tags: Linked List, Two Pointers

## 🎯 Problem Description
Find the node where two linked lists intersect.

## Examples
- Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
- Output: 8

## 💡 Solution Ideas
- Use **two pointers** traveling both lists.
- When a pointer reaches end, switch to the other list.
- They will meet at intersection or null.

## 📁 Code Files
- [Python Solution](get_intersection_node.py)
- [C++ Solution](get_intersection_node.cpp)

## ⚡ Complexity
- Time: O(m + n)
- Space: O(1)

## 📝 Training Log
- Completed Time: 2026-03-22
- Difficulty Evaluation: ⭐⭐
- Notes: Mastered two-pointer cross-traversal for linked list intersection.
