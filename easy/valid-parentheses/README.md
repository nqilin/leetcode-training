# Valid Parentheses (LeetCode 20)
**Difficulty**: Easy
**Link**: [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)

## Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples
- Input: "()" → Output: true
- Input: "()[]{}" → Output: true
- Input: "(]" → Output: false
- Input: "([)]" → Output: false
- Input: "{[]}" → Output: true

## Solution Idea: Stack
1. Use a **stack** to keep track of opening brackets.
2. Use a **dictionary** to map closing brackets to their matching opening brackets.
3. For each character:
   - If it is a closing bracket:
     - Pop the top element from the stack.
     - If they do NOT match → return false.
   - If it is an opening bracket:
     - Push it to the stack.
4. At the end, the stack must be **empty** (all opened brackets are closed).

## Complexity
- **Time Complexity**: O(n) — one pass through the string.
- **Space Complexity**: O(n) — stack can store up to n characters.

## Key Learnings
- Stack usage for matching/validation problems
- Dictionary mapping for quick lookup
- Common logic for parenthesis / bracket validation (interview classic)
