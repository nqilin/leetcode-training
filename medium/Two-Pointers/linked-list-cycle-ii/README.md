# [LeetCode 142 - Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
> Difficulty: Medium | Tags: Linked List, Two Pointers

## Problem Description
Given a linked list, return the node where the cycle begins. If no cycle, return null.

## Examples
- Input: head = [3,2,0,-4], pos = 1
- Output: node with value 2

## Solution Ideas
1. Use fast and slow pointers to detect cycle.
2. When they meet, move slow back to head.
3. Move both one step until they meet again at cycle entrance.

## Code Files
- [Python Solution](sslocal://flow/file_open?url=detect_cycle.py&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [C++ Solution](sslocal://flow/file_open?url=detect_cycle.cpp&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## Key Points
- Classic Floyd's cycle-finding algorithm
- Pure two-pointer solution with no extra space

## Training Log
- Completed Time: 2026-04-10
- Difficulty Evaluation: ⭐⭐
- Notes: Mastered two-pointer cycle detection in linked list
