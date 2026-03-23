# [LeetCode 234 - Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
> Difficulty: Easy | Tags: Linked List, Two Pointers

## 🎯 Problem Description
Check if a linked list is a palindrome.

## Examples
- Input: 1 -> 2 -> 2 -> 1
- Output: true

## 💡 Solution Ideas
1. Use fast & slow pointers to **find the middle**.
2. **Reverse the second half** of the list.
3. Compare first half and reversed second half.

## 📁 Code Files
- [Python Solution](is_palindrome.py)
- [C++ Solution](is_palindrome.cpp)

## ⚡ Complexity
- Time: O(n)
- Space: O(1)

## 📝 Training Log
- Completed Time: 2026-03-23
- Difficulty Evaluation: ⭐⭐
- Notes: Combined find middle + reverse list + palindrome check.
