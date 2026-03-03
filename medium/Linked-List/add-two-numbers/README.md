# [LeetCode 2 - Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
> Difficulty: Medium | Tags: Linked List, Math, Recursion

## 🎯 Problem Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
- You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807 (linked lists are in reverse order: 2→4→3 = 342, 5→6→4 = 465).

## 💡 Solution Ideas
1. Core Idea: Simulate manual addition (digit by digit + carry) with linked list traversal
2. Step-by-Step Explanation:
   - Use a **dummy node** to simplify result list construction (avoid edge case for head node)
   - Traverse both linked lists simultaneously, add corresponding digits + carry
   - Current digit = (val1 + val2 + carry) % 10, carry = (val1 + val2 + carry) // 10
   - Continue traversal until both lists are exhausted AND carry is 0 (critical for last digit carry)
   - Create new nodes for the sum digits and link them together
3. Edge Cases:
   - Different length lists (e.g., l1 = [9,9], l2 = [1] → sum = [0,0,1])
   - Final carry (e.g., l1 = [9,9,9], l2 = [9,9,9] → sum = [8,9,9,1])
   - Zero values (e.g., l1 = [0], l2 = [0] → sum = [0])

## 📁 Code Files
- [Python Solution](add_two_numbers.py)
- [C++ Solution](add_two_numbers.cpp)

## ⚡ Complexity Analysis
- **Time Complexity (TC)**: O(max(m, n)) 
  - m = length of l1, n = length of l2
  - Traverse the longer list once, each node processed exactly once
- **Space Complexity (SC)**: O(max(m, n))
  - Result list has at most max(m, n) + 1 nodes (extra node for final carry)
  - Only constant extra space (dummy node, current pointer, carry) besides result list

## 📌 Problem-Solving Tips
1. Key Trick: Dummy node avoids handling the head node separately (common linked list pattern)
2. Carry Handling: Must continue loop until carry is 0 (even if both lists are exhausted)
3. Length Difference: Use 0 for digits when one list is shorter than the other
4. Memory Management (C++): Remember to free dummy node memory (avoid memory leak)
5. Alternative Approach: Recursive solution (but iterative is more efficient for large lists)
6. Common Mistake: Forgetting the final carry (e.g., 999 + 999 = 1998, missing the leading 1)

## 📝 Training Log
- Completed Time: 2026-03-03
- Difficulty Evaluation: ⭐⭐⭐ (1-5 stars)
- Notes: Mastered basic linked list traversal and dummy node pattern; need to practice more complex linked list operations (reverse, merge)
