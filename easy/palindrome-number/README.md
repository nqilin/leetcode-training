# Palindrome Number (LeetCode 9)
**Difficulty**: Easy  
**Link**: [https://leetcode.com/problems/palindrome-number/](https://leetcode.com/problems/palindrome-number/)

## Problem Statement
Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

A number is palindrome when it reads the same forward and backward.

### Examples
- Input: x = 121 → Output: true
- Input: x = -121 → Output: false
- Input: x = 10 → Output: false
- Input: x = 0 → Output: true

### Constraints
- `-2^31 <= x <= 2^31 - 1`

## Solutions

### Solution 1: Convert to String (Beginner-Friendly)
- **Idea**: Turn integer into string, reverse it, and compare with original.
- **Time Complexity**: O(n) (n = number of digits)
- **Space Complexity**: O(n) (stores reversed string)
- **Pros**: Extremely simple, easy to write and understand.
- **Cons**: Uses extra space for string.

### Solution 2: Pure Math (No String, Optimal)
- **Idea**: Reverse the second half of the number using arithmetic only.
- **Time Complexity**: O(log x) (digits count)
- **Space Complexity**: O(1) (no extra space)
- **Pros**: No string conversion, efficient, professional.
- **Cons**: Slightly more logic for beginners.

## Key Edge Cases
- Negative numbers are never palindromes.
- Numbers ending in 0 (except 0 itself) are not palindromes.
- Single-digit numbers (0-9) are always palindromes.

## What You Learn
- String slicing `s[::-1]` (Python classic reverse)
- How to reverse a number using math (`% 10`, `// 10`)
- Palindrome definition & common edge cases
- Space-time tradeoff in algorithm design
