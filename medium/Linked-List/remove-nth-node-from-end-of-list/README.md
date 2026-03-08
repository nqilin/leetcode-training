# [LeetCode 19 - Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
> Difficulty: Medium | Tags: Linked List, Two Pointers

## 🎯 Problem Description
Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.
- Follow up: Could you do this in one pass?

Examples:
1. Input: head = [1,2,3,4,5], n = 2 → Output: [1,2,3,5]
2. Input: head = [1], n = 1 → Output: []
3. Input: head = [1,2], n = 1 → Output: [1]

## 💡 Solution Ideas
1. Core Idea: **Two Pointers (Fast & Slow) with n-gap** (one-pass solution)
   - Avoid two-pass solution (first count length, then remove node)
   - Create a gap of n nodes between fast and slow pointers
2. Step-by-Step Explanation:
   - Use a **dummy node** to handle edge case (removing the head node)
   - Initialize slow at dummy, fast at head
   - Move fast pointer n steps forward (create n-gap between slow and fast)
   - Move both pointers until fast reaches null (slow stops at the node BEFORE the target node)
   - Skip the target node (slow.next = slow.next.next)
   - Return dummy.next (modified list head)
3. Edge Cases:
   - Remove the head node (e.g., [1,2,3], n=3 → [2,3])
   - Remove the last node (e.g., [1,2], n=1 → [1])
   - Single node list (e.g., [1], n=1 → [])

## 📁 Code Files
- [Python Solution](remove_nth_node.py)
- [C++ Solution](remove_nth_node.cpp)

## ⚡ Complexity Analysis
- **Time Complexity (TC)**: O(L) 
  - L = length of the linked list (one-pass traversal)
  - Fast pointer moves L steps, slow pointer moves L-n steps (total O(L))
- **Space Complexity (SC)**: O(1) 
  - Only two pointers + dummy node (constant extra space)
  - Better than two-pass solution (same time complexity but one-pass is optimal)

## 📌 Problem-Solving Tips
1. Key Trick: Dummy node is essential to handle head removal (avoids null pointer exception)
2. Gap Creation: Fast pointer moves n steps first — this is the core of one-pass solution
3. Critical Position: Slow stops at the **previous node** of the target (so we can skip the target node)
4. Alternative Approach (Two-Pass):
   - First pass: count the length L of the list
   - Second pass: move to L-n-th node from start, remove it
   - Simpler but requires two traversals (not optimal)
5. Common Mistakes:
   - Forgetting dummy node (fails when removing head)
   - Moving slow to head instead of dummy (can't reach previous node of head)
   - Not handling single node list (leads to null pointer)

## 📝 Training Log
- Completed Time: 2026-03-08
- Difficulty Evaluation: ⭐⭐⭐ (1-5 stars)
- Notes: Mastered fast-slow pointer pattern for linked list end operations; understood the critical role of dummy node in edge cases
